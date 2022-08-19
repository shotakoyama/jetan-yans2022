import numpy as np

class BaseScorer:

    title = 'base'

    def __init__(self):
        self.tp = 0
        self.fp = 0
        self.fn = 0


class TypeScorer:

    title = 'type'
    labels = ['A', 'B', 'C']

    def __init__(self):
        self.cm = np.zeros(
                (len(self.labels), 3),
                dtype = np.int)

    def update_one(self, edit, result):
        x = self.get_label(edit)
        self.cm[x, result] += 1

