from .token import Token

class Sent(list):

    def __init__(self, token_list):
        super().__init__(token_list)

    def encode(self):
        return {'sent': [token.encode() for token in self]}

    @classmethod
    def decode(cls, dct):
        return cls([Token.decode(token) for token in dct['sent']])

    def __str__(self):
        text_list = [token.text for token in self]
        return ''.join(text_list)

    def make_front(self):
        front = 0
        for token in self:
            token.front = front
            front += len(token.text)
        return self

    def make_dependents(self):
        for token in self:
            if token.head != token.index:
                self[token.head].dependents.append(token.index)
        return self

    def get_bunsetu_list(self):
        lst = []

        for index, token in enumerate(self):
            if token.bunsetu == 'B':
                tmp = [index]
                lst.append(tmp)
            elif token.bunsetu == 'I':
                lst[-1].append(index)
            else:
                assert False

        return lst

    def get_bunsetu_spans(self):
        bunsetu_list = self.get_bunsetu_list()
        bunsetu_spans = []

        for bunsetu in bunsetu_list:
            assert len(bunsetu) > 0
            start = bunsetu[0]
            end = bunsetu[-1]
            bunsetu_spans.append((start, end + 1))

        return bunsetu_spans

