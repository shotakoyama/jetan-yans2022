from .scorer import (
        TypeScorer,
        CMScorer)
from .scorer_attr import TypeScorerAttr
from .update import (
        update_type_count,
        update_cm_count)

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


attr = TypeScorerAttr('unit', ['O', 'L', 'G', 'I', 'Y'])


class UnitScorer(TypeScorer):

    attr = attr

    def update_pair(self, ref_edits, hyp_edits):
        update_type_count(
                self,
                ref_edits,
                hyp_edits,
                edits_to_tuple)


class UnitCMScorer(CMScorer):

    attr = attr

    def update_pair(self, ref_edits, hyp_edits):
        update_cm_count(
                self,
                ref_edits,
                hyp_edits,
                edits_to_tuple)

