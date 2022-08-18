from .select_util import (
        is_punct,
        is_punct_or_func,
        bunsetu_head)
from .select_list import SelectList

class StartList(SelectList):

    def __init__(self, corr, trg, edit_list):
        self.corr = corr
        self.src = corr.src
        self.trg = trg
        self.edit_list = edit_list
        super().__init__(self.init_start_list())

    def init_start_list(self):
        start_pos = 0
        first_head = True
        multi_path = False

        start_list = []

        for index, edit in enumerate(self.edit_list):
            src_tokens = self.src[edit.src_start : edit.src_end]
            trg_tokens = self.trg[edit.trg_start : edit.trg_end]

            if bunsetu_head(trg_tokens):
                if first_head:
                    first_head = False
                else:
                    start_pos = start_pos + 1
                    multi_path = False
            else:
                if edit.form != 'N' and not is_punct_or_func(self.src, self.trg, edit):
                    multi_path = True

            if multi_path:
                start_list.append([start_pos, start_pos + 1])
            else:
                start_list.append([start_pos])

        return start_list

    def merge_noop(self):
        for i, edit in list(enumerate(self.edit_list))[::-1]:
            if edit.form == 'N' and len(self[i]) >= 2:
                if not is_punct(self.src, self.trg, edit):
                    self[i] = self[i][0:1]

    def deletion(self):
        for i, edit in enumerate(self.edit_list):
            if edit.form == 'U' and len(self[i]) >= 2:
                if not is_punct_or_func(self.src, self.trg, edit):
                    src_tokens = self.src[edit.src_start : edit.src_end]
                    if bunsetu_head(src_tokens):
                        self[i] = self[i][1:]

    def make(self):
        self.merge_noop()
        self.min_max_sup()
        self.deletion()
        self.min_max_sup()
        self.select_top()

