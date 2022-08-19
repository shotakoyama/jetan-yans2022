from .scorer import BaseScorer
from .update import (
        update_score,
        update_count)
from .scorer_util import show_scorer

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


class FullScorer(BaseScorer):

    title = 'full'

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

    def update(self, data):
        update_score(self, data)
        return self

    def show(self):
        show_scorer(self)

