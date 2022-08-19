from .scorer import TypeScorer
from .update import (
        update_score,
        update_type_count)
from .scorer_util import show_type_scorer

def edits_to_tuple(edits):
    tuples = {(
        edit.unit,
        edit.src_start,
        edit.src_end,
        edit.trg_start,
        edit.trg_end)
        for edit
        in edits}
    return tuples


class UnitScorer(TypeScorer):

    title = 'unit'
    labels = ['O', 'L', 'G', 'I', 'Y']
    label_dict = {
            label: index
            for index, label
            in enumerate(labels)}

    def get_label(self, x):
        return self.label_dict[x[0]]

    def update_pair(self, ref_edits, hyp_edits):
        update_type_count(
                self,
                ref_edits,
                hyp_edits,
                edits_to_tuple)

    def update(self, data):
        update_score(self, data)
        return self

    def show(self):
        show_type_scorer(self)

