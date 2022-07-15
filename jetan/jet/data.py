from .corr import JetCorr

class JetData:

    def __init__(self, corrs):
        self.corrs = corrs

    def encode(self):
        text = '\n\n'.join([
            '# {}\n'.format(index) + corr.encode()
            for index, corr
            in enumerate(self.corrs, start = 1)])
        return text

    @classmethod
    def decode(cls, text):
        corrs = [
            JetCorr.decode(corr)
            for corr
            in text.split('\n\n')]
        return cls(corrs)

