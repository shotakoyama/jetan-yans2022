from prettytable import PrettyTable
from .scorer import BaseScorer
from .update import (
        update_score,
        update_count)
from .scorer_util import show_scorer

def edits_to_spans(edits):
    spans = {(
        edit.src_start,
        edit.src_end,
        edit.trg_start,
        edit.trg_end)
        for edit
        in edits}
    return spans


class SpanScorer(BaseScorer):

    title = 'span'

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

    def update(self, data):
        update_score(self, data)
        return self

    def show(self):
        show_scorer(self)

