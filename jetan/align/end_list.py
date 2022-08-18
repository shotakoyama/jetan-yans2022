from .select_util import (
        get_edit_source,
        is_punct,
        is_punct_or_func,
        bunsetu_head)
from .select_list import SelectList

class EndList(SelectList):

    def __init__(self, corr, trg, edit_list, start_list):
        self.corr = corr
        self.src = corr.src
        self.trg = trg
        self.edit_list = edit_list
        super().__init__(self.init_end_list(start_list))

    def init_end_list(self, start_list):
        end_list = [
                [x, x + 1]
                for x
                in start_list]
        return end_list

    def noop_cond(self):
        for i, edit in enumerate(self.edit_list):
            if edit.form != 'U' and len(self[i]) >= 2:
                self[i] = self[i][1:]

    def is_src_tail(self, edit, end):
        if len(end) > 1:
            return False

        src_tokens = get_edit_source(self.src, edit)
        if len(src_tokens) == 0:
            return False

        if any(x.tag1 == '補助記号' for x in src_tokens):
            return False

        return src_tokens[0].bunsetu == 'I'

    def next_I_cond(self):
        src_tail = False

        for i, edit in list(enumerate(self.edit_list))[::-1]:
            if src_tail and len(self[i]) >= 2:
                self[i] = self[i][1:]
            src_tail = self.is_src_tail(edit, self[i])

    def make(self):
        self.noop_cond()
        self.min_max_sup()
        self.next_I_cond()
        self.min_max_sup()
        self.select_top()

