class Edit:

    def __init__(self, ss, se, ts, te):
        self.src_start = ss
        self.src_end = se
        self.trg_start = ts
        self.trg_end = te

    def comes_just_before(self, other):
        return (
            (self.src_end == other.src_start)
            and
            (self.trg_end == other.trg_start))

    def mergeable(self, other):
        assert self.src_end == other.src_start
        assert self.trg_end == other.trg_start

    def get_merging_class(self, other):
        return Edit

    def __add__(self, other):
        self.mergeable(other)
        merging_class = self.get_merging_class(other)
        edit = merging_class(
                self.src_start,
                other.src_end,
                self.trg_start,
                other.trg_end)
        return edit

    def src_repr(self):
        if self.src_start == self.src_end:
            x = '{}'.format(self.src_start)
        else:
            x = '({}, {})'.format(
                    self.src_start,
                    self.src_end)
        return x

    def trg_repr(self):
        if self.trg_start == self.trg_end:
            x = '{}'.format(self.trg_start)
        else:
            x = '({}, {})'.format(
                    self.trg_start,
                    self.trg_end)
        return x

    def __repr__(self):
        line = '{}-{}-{}'.format(
                self.src_repr(),
                self.form,
                self.trg_repr())
        return line


class NoopEdit(Edit):

    noop = True
    form = 'N'

    def get_merging_class(self, other):
        if type(other) == NoopEdit:
            x = NoopEdit
        else:
            x = ReplaceEdit
        return x


class OpEdit(Edit):

    noop = False


class ReplaceEdit(OpEdit):

    form = 'R'

    def get_merging_class(self, other):
        return ReplaceEdit


class UnnecessaryEdit(OpEdit):

    form = 'U'

    def get_merging_class(self, other):
        if type(other) == UnnecessaryEdit:
            x = UnnecessaryEdit
        else:
            x = ReplaceEdit
        return x


class MissingEdit(OpEdit):

    form = 'M'

    def get_merging_class(self, other):
        if type(other) == MissingEdit:
            x = MissingEdit
        else:
            x = ReplaceEdit
        return x

