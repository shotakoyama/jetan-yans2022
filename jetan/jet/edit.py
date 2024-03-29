class JetEdit:

    def __init__(
            self,
            index,
            start,
            end,
            form,
            unit,
            text,
            note = '_'):

        assert '\t' not in text

        self.index = index
        self.start = start
        self.end = end
        self.form = form
        self.unit = unit
        self.text = text
        self.note = note

    def encode(self, head = 'A'):
        line = '\t'.join([
            head,
            str(self.index),
            str(self.start),
            str(self.end),
            self.form,
            self.unit,
            self.text,
            self.note])
        return line

    @classmethod
    def decode(cls, line):
        lst = line.split('\t')
        index = int(lst[1])
        start = int(lst[2])
        end = int(lst[3])
        form = lst[4]
        unit = lst[5]
        text = lst[6]
        note = lst[7]
        return cls(
                index,
                start,
                end,
                form,
                unit,
                text,
                note)

    def span_eq(self, other):
        return (
            (self.start == other.start)
            and
            (self.end == other.end)
            and
            (self.text == other.text))

    def span_lt(self, other):
        if self.start < other.start:
            return True
        if self.end < other.end:
            return True
        return self.text < other.text

