def blank(x):
    if x is None:
        x = '____'
    return x

def get_index(token):
    return str(token.index)


def get_text(token):
    return token.text


def get_tag1(token):
    return token.tag1


def get_tag2(token):
    return blank(token.tag2)


def get_tag3(token):
    return blank(token.tag3)


def get_tag4(token):
    return blank(token.tag4)


def get_pos(token):
    return token.pos


def get_dep(token):
    return token.dep


def get_head(token):
    return str(token.head)


def get_lemma(token):
    return token.lemma


def get_norm(token):
    return token.norm


def get_bunsetu(token):
    return token.bunsetu


def get_ner(token):
    return token.ner


def get_ner_iob(token):
    return token.ner_iob


def get_yomi(token):
    return token.yomi


def get_kata(token):
    return blank(token.kata)


def get_gyogo(token):
    return blank(token.gyogo)


def get_infl(token):
    return blank(token.infl)


def get_onbin(token):
    return blank(token.onbin)


def get_front(token):
    return str(token.front)

def get_dependants(token):
    return ','.join([str(x) for x in token.dependents])


class Row:

    def __init__(self, token):
        self.token = token


    def __call__(self):
        return (
            get_index(self.token),
            get_text(self.token),
            get_tag1(self.token),
            get_tag2(self.token),
            get_tag3(self.token),
            get_tag4(self.token),
            get_pos(self.token),
            get_dep(self.token),
            get_head(self.token),
            get_lemma(self.token),
            get_norm(self.token),
            get_bunsetu(self.token),
            get_ner(self.token),
            get_ner_iob(self.token),
            get_yomi(self.token),
            get_kata(self.token),
            get_gyogo(self.token),
            get_infl(self.token),
            get_onbin(self.token),
            get_front(self.token),
            get_dependants(self.token))

