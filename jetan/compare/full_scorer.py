from .scorer import SingleScorer
from .scorer_attr import ScorerAttr
from .update import update_count

def edits_to_full(edits):
    spans = {(
        edit.form,
        edit.unit,
        edit.src_start,
        edit.src_end,
        edit.trg_start,
        edit.trg_end)
        for edit
        in edits}
    return spans


class FullScorer(SingleScorer):

    attr = ScorerAttr('full')

    def update_pair(
            self,
            ref_edits,
            hyp_edits):

        update_count(
                self,
                ref_edits,
                hyp_edits,
                edits_to_full)
        return self

