class Token:

    def __init__(self,
            index,
            text = None,
            tag1 = None,
            tag2 = None,
            tag3 = None,
            tag4 = None,
            pos = None,
            dep = None,
            head = None,
            lemma = None,
            norm = None,
            bunsetu = None,
            ner = None,
            ner_iob = None,
            yomi = None,
            kata = None,
            gyogo = None,
            infl = None,
            onbin = None,
            front = None,
            dependents = None):

        self.index = index
        self.text = text
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3
        self.tag4 = tag4
        self.pos = pos
        self.dep = dep
        self.head = head
        self.lemma = lemma
        self.norm = norm
        self.bunsetu = bunsetu
        self.ner = ner
        self.ner_iob = ner_iob
        self.yomi = yomi
        self.kata = kata
        self.gyogo = gyogo
        self.infl = infl
        self.onbin = onbin
        self.front = front

        if dependents is None:
            self.dependents = []
        else:
            self.dependents = dependents

    def encode(self):
        dct = {
            'index': self.index,
            'text': self.text,
            'tag1': self.tag1,
            'tag2': self.tag2,
            'tag3': self.tag3,
            'tag4': self.tag4,
            'pos': self.pos,
            'dep': self.dep,
            'head': self.head,
            'lemma': self.lemma,
            'norm': self.norm,
            'bunsetu': self.bunsetu,
            'ner': self.ner,
            'ner_iob': self.ner_iob,
            'yomi': self.yomi,
            'kata': self.kata,
            'gyogo': self.gyogo,
            'infl': self.infl,
            'onbin': self.onbin,
            'front': self.front,
            'dependents': self.dependents}
        return dct

    @classmethod
    def decode(cls, dct):
        token = cls(
            index = dct['index'],
            text = dct['text'],
            tag1 = dct['tag1'],
            tag2 = dct['tag2'],
            tag3 = dct['tag3'],
            tag4 = dct['tag4'],
            pos = dct['pos'],
            dep = dct['dep'],
            head = dct['head'],
            lemma = dct['lemma'],
            norm = dct['norm'],
            bunsetu = dct['bunsetu'],
            ner = dct['ner'],
            ner_iob = dct['ner_iob'],
            yomi = dct['yomi'],
            kata = dct['kata'],
            gyogo = dct['gyogo'],
            infl = dct['infl'],
            onbin = dct['onbin'],
            front = dct['front'],
            dependents = dct['dependents'])
        return token

