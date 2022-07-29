def edits_to_spans(edits):
    spans = {
        edit.get_span()
        for edit
        in edits}
    return spans


class Scorer:

    def __init__(self):
        self.match = 0
        self.n_ref = 0
        self.n_hyp = 0

    def update(self, ref_edits, hyp_edits):
        ref_spans = edits_to_spans(ref_edits)
        hyp_spans = edits_to_spans(hyp_edits)
        self.match += len(ref_spans & hyp_spans)
        self.n_ref += len(ref_spans)
        self.n_hyp += len(hyp_spans)

    def show(self):
        line = 'match: {},\tn_ref: {},\tn_hyp: {}'.format(self.match, self.n_ref, self.n_hyp)
        print(line)

        if self.n_hyp == 0:
            p = 1.0
        else:
            p = self.match / self.n_hyp

        if self.n_ref == 0:
            r = 0
        else:
            r = self.match / self.n_ref

        f = 2 * p * r / (p + r)
        line = 'P: {:.2f},\tR: {:.2f},\tF: {:.2f}'.format(p * 100, r * 100, f * 100)
        print(line)


class TagScorer:

    def __init__(self):
        self.match = {tag: 0 for tag in self.tags}
        self.n_ref = {tag: 0 for tag in self.tags}

    def update(self, ref_edits, hyp_edits):
        hyp_spans = edits_to_spans(hyp_edits)

        for tag in self.tags:
            ref_spans = {
                    edit.get_span()
                    for edit
                    in ref_edits
                    if self.cond(edit, tag)}
            self.match[tag] += len(hyp_spans & ref_spans)
            self.n_ref[tag] += len(ref_spans)

    def show(self):
        lst = ['{}: {}/{}'.format(tag, self.match[tag], self.n_ref[tag]) for tag in self.tags]
        print(',\t'.join(lst))


class FormScorer(TagScorer):

    tags = list('MUFC')

    def cond(self, edit, form):
        return edit.form == form


class UnitScorer(TagScorer):

    tags = list('OLGI')

    def cond(self, edit, unit):
        return edit.unit == unit

