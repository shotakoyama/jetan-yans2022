class ScorerAttr:

    def __init__(self, title):
        self.title = title


class TypeScorerAttr(ScorerAttr):

    def __init__(self, title, labels):
        super().__init__(title)
        self.labels = labels
        self.label_dict = {
                label: index
                for index, label
                in enumerate(labels)}

    def get_label(self, x):
        return self.label_dict[x[0]]

