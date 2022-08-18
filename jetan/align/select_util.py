def join_tokens(tokens):
    return '_'.join([x.text for x in tokens])


def get_edit_source(src, edit):
    tokens = src[edit.src_start : edit.src_end]
    return tokens


def get_edit_target(trg, edit):
    tokens = trg[edit.trg_start : edit.trg_end]
    return tokens


def is_pos(src, trg, edit, pos_dict):
    src_tokens = src[edit.src_start : edit.src_end]
    trg_tokens = trg[edit.trg_start : edit.trg_end]

    if any(x.tag1 in pos_dict for x in src_tokens):
        return True

    if any(x.tag1 in pos_dict for x in trg_tokens):
        return True

    return False


def is_punct(src, trg, edit):
    return is_pos(src, trg, edit, {'補助記号'})


def is_punct_or_func(src, trg, edit):
    return is_pos(src, trg, edit, {'補助記号', '助詞', '助動詞'})


def bunsetu_head(tokens):
    return len(tokens) > 0 and tokens[0].bunsetu == 'B'


def min_sup(lst, init_min = 0):
    min_tmp = init_min
    for i in range(len(lst)):
        lst[i] = [
            x
            for x
            in lst[i]
            if x >= min_tmp]
        min_tmp = min(lst[i])
    return lst


def max_sup(lst, init_max = 1000000):
    max_tmp = init_max
    for i in range(len(lst))[::-1]:
        lst[i] = [
            x
            for x
            in lst[i]
            if x <= max_tmp]
        max_tmp = max(lst[i])
    return lst


def min_max_sup(lst, init_min = 0, init_max = 1000000):
    lst = min_sup(lst, init_min)
    lst = max_sup(lst, init_max)
    return lst

