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

