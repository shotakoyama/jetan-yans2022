from .sent import Sent

class Corr:

    def __init__(self, src, trgs):
        self.src = src
        self.trgs = trgs

    def encode(self):
        src = self.src.encode()
        trgs = [trg.encode() for trg in self.trgs]
        return {'src': src, 'trgs': trgs}

    @classmethod
    def decode(cls, dct):
        src = Sent.decode(dct['src'])
        trgs = [Sent.decode(trg) for trg in dct['trgs']]
        return cls(src, trgs)

