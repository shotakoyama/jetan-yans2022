import spacy
import ginza

def load_nlp(name, mode):
    nlp = spacy.load(name)
    ginza.set_split_mode(nlp, mode)
    return nlp

