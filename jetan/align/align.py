from .dist_array import DistArray
from .edit_util import (
        make_edit_list,
        merge_edits)
from jetan.jet.edit import JetEdit
from jetan.jet.corr import JetCorr
from .form import get_form
from .unit import get_unit

class Aligner:

    def __init__(self, dist, corr):
        self.dist = dist
        self.corr = corr

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

    def get_edit_text(self, trg, edit):
        ts = edit.trg_start
        te = edit.trg_end
        return ''.join(token.text for token in trg[ts : te])

    def make_jet_edit(self, anno_id, trg, edit):
        start, end = self.get_source_start_end(edit)
        form = get_form(self.corr.src, trg, edit)
        unit = get_unit(self.corr.src, trg, edit)
        text = self.get_edit_text(trg, edit)
        jet_edit = JetEdit(
                anno_id,
                start,
                end,
                form,
                unit,
                text)
        return jet_edit

    def get_edits(self, anno_id, trg):
        arr = DistArray(self.dist, self.corr.src, trg)
        edit_list = make_edit_list(arr)
        edit_list = merge_edits(arr, edit_list)
        edit_list = [
                self.make_jet_edit(anno_id, trg, edit)
                for edit
                in edit_list]
        return edit_list

    def make_jet_corr(self):
        src = str(self.corr.src)
        trgs = [str(trg) for trg in self.corr.trgs]
        edits = [
            edit
            for anno_id, trg
            in enumerate(self.corr.trgs, start = 1)
            for edit
            in self.get_edits(anno_id, trg)]
        return JetCorr(src, trgs, edits)

