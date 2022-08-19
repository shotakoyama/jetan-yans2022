class CompEdit:

    def __init__(self, edit, offset):
        self.edit = edit
        self.src_start = edit.start
        self.src_end = edit.end
        self.trg_start = self.src_start + offset
        self.trg_end = self.trg_start + len(edit.text)
        self.form = edit.form
        self.unit = edit.unit

    def __repr__(self):
        tup = (
            self.src_start,
            self.src_end,
            self.trg_start,
            self.trg_end,
            self.form,
            self.unit,
            self.edit.text)
        return str(tup)

