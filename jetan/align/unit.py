def lexical_cond_1(src_tokens, trg_tokens):
    if len(src_tokens) != 1:
        return False

    if len(trg_tokens) != 1:
        return False

    if src_tokens[0].tag1 in {'補助記号', '助詞', '助動詞'}:
        return False

    return src_tokens[0].tag1 == trg_tokens[0].tag1

def get_unit(src, trg, edit):
    src_tokens = src[edit.src_start : edit.src_end]
    trg_tokens = trg[edit.trg_start : edit.trg_end]

    if all([x.tag1 == '補助記号' for x in src_tokens + trg_tokens]):
        unit = 'O'
    elif lexical_cond_1(src_tokens, trg_tokens):
        unit = 'L'
    else:
        unit = 'G'

    return unit

