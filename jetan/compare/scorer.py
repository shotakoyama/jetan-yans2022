import numpy as np
from .scorer_util import (
        show_scorer,
        show_type_scorer,
        show_cm_scorer)

class BaseScorer:

    attr = None

    def update_corr(self, corr):
        for dct in corr:
            ref_edits = dct['ref']
            hyp_edits = dct['hyp']
            self.update_pair(ref_edits, hyp_edits)

    def update(self, data):
        for corr in data:
            self.update_corr(corr)
        return self


class SingleScorer(BaseScorer):

    def __init__(self):
        self.tp = 0 # true positive
        self.fp = 0 # false positive
        self.fn = 0 # false negative

    def show(self):
        show_scorer(self)


class TypeScorer(BaseScorer):

    def __init__(self):
        # 1. (labels)
        # 2. (true positive, false positive, false negative)
        self.array = np.zeros(
                (len(self.attr.labels), 3),
                dtype = np.int)

    def update_one(self, edit, result):
        x = self.attr.get_label(edit)
        self.array[x, result] += 1

    def show(self):
        show_type_scorer(self)


class CMScorer(BaseScorer):

    attr = None

    def __init__(self):
        # confusion matrix
        # 1. reference
        # 2. hypothesis
        self.cm = np.zeros(
                (len(self.attr.labels),) * 2,
                dtype = np.int)

    def update_one(self, ref, hyp):
        ref_index = self.attr.get_label(ref)
        hyp_index = self.attr.get_label(hyp)
        self.cm[ref_index, hyp_index] += 1

    def show(self):
        show_cm_scorer(self)

