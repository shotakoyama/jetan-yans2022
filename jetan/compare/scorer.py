class Scorer:

    def __init__(self):
        self.match = 0
        self.n_ref = 0
        self.n_hyp = 0

    def update(self, ref_edits, hyp_edits):
        ref_spans = {
                edit.get_span()
                for edit
                in ref_edits}
        hyp_spans = {
                edit.get_span()
                for edit
                in hyp_edits}
        self.match += len(ref_spans & hyp_spans)
        self.n_ref += len(ref_spans)
        self.n_hyp += len(hyp_spans)

    def show(self):
        print('match: {}'.format(self.match))
        print('n_ref: {}'.format(self.n_ref))
        print('n_hyp: {}'.format(self.n_hyp))

        p = self.match / self.n_hyp
        r = self.match / self.n_ref
        f = 2 * p * r / (p + r)
        print('p: {:.2f}'.format(p * 100))
        print('r: {:.2f}'.format(r * 100))
        print('f: {:.2f}'.format(f * 100))


class FormScorer:

    def __init__(self):
        self.forms = list('MUFC')
        self.match = {form: 0 for form in self.forms}
        self.n_ref = {form: 0 for form in self.forms}

    def update(self, ref_edits, hyp_edits):
        hyp_spans = {
                edit.get_span()
                for edit
                in hyp_edits}

        for form in self.forms:
            ref_spans = {
                    edit.get_span()
                    for edit
                    in ref_edits
                    if edit.form == form}
            self.match[form] += len(hyp_spans & ref_spans)
            self.n_ref[form] += len(ref_spans)

    def show(self):
        print(self.match)
        print(self.n_ref)


class UnitScorer:

    def __init__(self):
        self.units = list('OLGI')
        self.match = {unit: 0 for unit in self.units}
        self.n_ref = {unit: 0 for unit in self.units}

    def update(self, ref_edits, hyp_edits):
        hyp_spans = {
                edit.get_span()
                for edit
                in hyp_edits}

        for unit in self.units:
            ref_spans = {
                    edit.get_span()
                    for edit
                    in ref_edits
                    if edit.unit == unit}
            self.match[unit] += len(hyp_spans & ref_spans)
            self.n_ref[unit] += len(ref_spans)

    def show(self):
        print(self.match)
        print(self.n_ref)

