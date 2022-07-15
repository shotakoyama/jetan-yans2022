from .dist_array import DistArray
from .edit_util import (
        make_edit_list,
        merge_edits)

def format_annotation(anno_id, start, end, form, unit, edit_trg, note):
    line = '\t'.join([
        'A',
        str(anno_id),
        str(start),
        str(end),
        form,
        unit,
        edit_trg,
        note])
    return line


class Aligner:

    def __init__(self, dist, corr):
        self.dist = dist
        self.corr = corr

    def generate_header(self, index):
        return '# {}'.format(index)

    def show_header(self, index):
        print(self.generate_header(index))

    def generate_source(self):
        return 'S\t{}'.format(str(self.corr.src))

    def show_source(self):
        print(self.generate_source())

    def generate_targets(self):
        lst = ['C\t{}'.format(str(trg)) for trg in self.corr.trgs]
        return '\n'.join(lst)

    def show_targets(self):
        print(self.generate_targets())

    def get_source_start_end(self, edit):
        ss = edit.src_start
        se = edit.src_end

        if ss < len(self.corr.src):
            start = self.corr.src[ss].front
        else:
            start = len(str(self.corr.src))

        if se < len(self.corr.src):
            end = self.corr.src[se].front
        else:
            end = len(str(self.corr.src))

        return start, end

    def get_edit_trg(self, trg, edit):
        ts = edit.trg_start
        te = edit.trg_end
        return ''.join(token.text for token in trg[ts : te])

    def show_annotation(self, anno_id, trg):
        arr = DistArray(self.dist, self.corr.src, trg)
        edit_list = make_edit_list(arr)
        edit_list = merge_edits(arr, edit_list)

        for edit in edit_list:
            start, end = self.get_source_start_end(edit)
            form = 'X'
            unit = 'Y'
            edit_trg = self.get_edit_trg(trg, edit)
            note = '_'
            anno = format_annotation(
                    anno_id,
                    start,
                    end,
                    form,
                    unit,
                    edit_trg,
                    note)
            print(anno)

    def show_annotations(self):
        for anno_id, trg in enumerate(self.corr.trgs, start = 1):
            self.show_annotation(anno_id, trg)

