from .char_dist import char_dist

def misform_cond_1(src_tokens, trg_tokens):
    if len(src_tokens) != 1 or len(trg_tokens) != 1:
        return False

    src, trg = src_tokens[0], trg_tokens[0]

    if src.tag1 != trg.tag1:
        return False

    if src.tag1 not in {'動詞', '助動詞'}:
        return False

    return src.lemma == trg.lemma or src.norm == trg.norm or src.yomi == trg.yomi


def misform_cond_2(src_tokens, trg_tokens):
    src_yomi = ''.join([x.yomi for x in src_tokens])
    trg_yomi = ''.join([x.yomi for x in trg_tokens])

    dist = char_dist(src_yomi, trg_yomi)
    norm = dist / max(len(src_yomi), len(trg_yomi))

    return norm <= 0.3


def get_form(src, trg, edit):
    src_tokens = src[edit.src_start : edit.src_end]
    trg_tokens = trg[edit.trg_start : edit.trg_end]

    if len(src_tokens) == 0:
        form = 'M'
    elif len(trg_tokens) == 0:
        form = 'U'
    elif misform_cond_1(src_tokens, trg_tokens):
        form = 'F'
    elif misform_cond_2(src_tokens, trg_tokens):
        form = 'F'
    else:
        form = 'C'

    return form

