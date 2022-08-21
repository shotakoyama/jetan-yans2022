from .char_dist import char_dist

def ortho_cond_1(src_tokens, trg_tokens):
    return all([x.tag1 == '補助記号' for x in src_tokens + trg_tokens])


def ortho_cond_2(src_tokens, trg_tokens):
    src_yomi = ''.join([x.yomi for x in src_tokens])
    trg_yomi = ''.join([x.yomi for x in trg_tokens])

    dist = char_dist(src_yomi, trg_yomi)
    norm = dist / max(len(src_yomi), len(trg_yomi))

    return norm < 0.3


def grammar_cond_1(src_tokens, trg_tokens):
    if len(src_tokens) != 1:
        return False

    if len(trg_tokens) != 1:
        return False

    src = src_tokens[0]
    trg = trg_tokens[0]

    if src.tag1 != trg.tag1:
        return False

    if src.tag1 not in {'動詞', '助動詞'}:
        return False

    if src.lemma == trg.lemma:
        return True

    if src.norm == trg.norm:
        return True

    if src.yomi == trg.yomi:
        return True

    return False


def grammar_cond_2(trg_tokens):
    return all(
            x.tag1 in {'助詞', '助動詞'}
            or x.dep == 'fixed'
            for x
            in  trg_tokens)


def lexical_cond_1(src_tokens, trg_tokens):
    if len(src_tokens) != 1:
        return False

    if len(trg_tokens) != 1:
        return False

    src = src_tokens[0]
    trg = trg_tokens[0]

    if src.tag1 in {'補助記号', '助詞', '助動詞'}:
        return False

    return src.tag1 == trg.tag1


def idiom_cond_1(src_tokens, trg_tokens):
    if len(src_tokens) >= 2:
        return True

    if len(trg_tokens) >= 2:
        return True

    return False


def get_unit(src, trg, edit):
    src_tokens = src[edit.src_start : edit.src_end]
    trg_tokens = trg[edit.trg_start : edit.trg_end]

    if ortho_cond_1(src_tokens, trg_tokens):
        unit = 'O'
    elif grammar_cond_1(src_tokens, trg_tokens):
        unit = 'G'
    elif ortho_cond_2(src_tokens, trg_tokens):
        unit = 'O'
    elif lexical_cond_1(src_tokens, trg_tokens):
        unit = 'L'
    elif grammar_cond_2(trg_tokens):
        unit = 'G'
    elif idiom_cond_1(src_tokens, trg_tokens):
        return 'I'
    else:
        unit = 'G'

    return unit

