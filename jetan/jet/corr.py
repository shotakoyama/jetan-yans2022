from .edit import JetEdit

class JetCorr:

    def __init__(
            self,
            src,
            trgs,
            edits):

        self.src = src
        self.trgs = trgs
        self.edits = edits

    def encode(self):
        src_line = 'S\t{}'.format(self.src)
        trg_lines = [
                'C\t{}'.format(trg)
                for trg
                in self.trgs]

        lst = [src_line]
        lst = lst + trg_lines
        lst = lst + [edit.encode() for edit in self.edits]

        text = '\n'.join(lst)
        return text

    @classmethod
    def decode(cls, text):

        trgs = []
        edits = []

        for line in text.split('\n'):

            if line.startswith('S'):

                lst = line.split('\t')
                assert len(lst) == 2
                src = lst[1]

            elif line.startswith('C'):

                lst = line.split('\t')
                assert len(lst) == 2
                trg = lst[1]
                trgs.append(trg)

            elif line.startswith('A'):

                edit = JetEdit.decode(line)
                edits.append(edit)

            else:
                pass

        return cls(src, trgs, edits)

