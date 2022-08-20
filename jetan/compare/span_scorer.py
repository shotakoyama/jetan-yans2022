from .scorer import SingleScorer
from .scorer_attr import ScorerAttr
from .update import update_count

def edits_to_spans(edits):
    spans = {(
        edit.src_start,
        edit.src_end,
        edit.trg_start,
        edit.trg_end)
        for edit
        in edits}
    return spans


class SpanScorer(SingleScorer):

    attr = ScorerAttr('span')

    def update_pair(
            self,
            ref_edits,
            hyp_edits):

        update_count(
                self,
                ref_edits,
                hyp_edits,
                edits_to_spans)
        return self

