from jetan.util.nlp import load_nlp
from jetan.util.token import Token
from jetan.util.sent import Sent

def tokenize(nlp, sent):
    doc = nlp(sent)
    token_list = [token for token in doc]
    bunsetu_list = doc.user_data['bunsetu_bi_labels']
    return token_list, bunsetu_list


def get_tag(token):
    x = token.tag_.split('-')

    if len(x) == 1:
        tag1, tag2, tag3, tag4 = x[0], None, None, None
    elif len(x) == 2:
        tag1, tag2, tag3, tag4 = x[0], x[1], None, None
    elif len(x) == 3:
        tag1, tag2, tag3, tag4 = x[0], x[1], x[2], None
    elif len(x) == 4:
        tag1, tag2, tag3, tag4 = x[0], x[1], x[2], x[3]
    else:
        assert False

    return tag1, tag2, tag3, tag4


def get_morph(token):
    dct = token.morph.to_dict()

    if 'Reading' in dct:
        yomi = dct['Reading']
    else:
        yomi = None

    if 'Inflection' in dct:
        katagyogo, inflonbin = dct['Inflection'].split(';')
        katagyogo = katagyogo.split('-')
        inflonbin = inflonbin.split('-')

        if len(katagyogo) == 1:
            kata, gyogo = katagyogo[0], None
        elif len(katagyogo) == 2:
            kata, gyogo = katagyogo
        else:
            assert False

        if len(inflonbin) == 1:
            infl, onbin = inflonbin[0], None
        elif len(inflonbin) == 2:
            infl, onbin = inflonbin
        else:
            assert False

    else:
        kata, gyogo, infl, onbin = None, None, None, None

    return yomi, kata, gyogo, infl, onbin


class Preproc:

    def __init__(self, name, mode):
        self.nlp = load_nlp(name, mode)

    def make_token(self, token, bunsetu):
        tag1, tag2, tag3, tag4 = get_tag(token)
        yomi, kata, gyogo, infl, onbin = get_morph(token)
        token = Token(
            index = token.i,
            text = token.text,
            tag1 = tag1,
            tag2 = tag2,
            tag3 = tag3,
            tag4 = tag4,
            pos = token.pos_,
            dep = token.dep_,
            head = token.head.i,
            lemma = token.lemma_,
            norm = token.norm_,
            bunsetu = bunsetu,
            ner = token.ent_type_,
            ner_iob = token.ent_iob_,
            yomi = yomi,
            kata = kata,
            gyogo = gyogo,
            infl = infl,
            onbin = onbin)
        return token

    def __call__(self, sent):
        sent, bunsetu_list = tokenize(self.nlp, sent)
        sent = [
            self.make_token(token, bunsetu)
            for token, bunsetu
            in zip(sent, bunsetu_list)]
        sent = Sent(sent)
        sent = sent.make_front()
        sent = sent.make_dependents()
        return sent

