from .corr import JetCorr

class JetData(list):

    def encode(self):
        text = '\n\n'.join([
            '# {}\n'.format(index) + corr.encode()
            for index, corr
            in enumerate(self, start = 1)])
        return text

    @classmethod
    def decode(cls, text):
        corrs = [
            JetCorr.decode(corr)
            for corr
            in text.split('\n\n')]
        return cls(corrs)

