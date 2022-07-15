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

    def __add__(self, other):
        assert self.src_end == other.src_start
        assert self.trg_end == other.trg_start
        edit = Edit(
            self.src_start,
            other.src_end,
            self.trg_start,
            other.trg_end)
        return edit

