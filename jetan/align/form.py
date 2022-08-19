
def get_form(src, trg, edit):
    src_tokens = src[edit.src_start : edit.src_end]
    trg_tokens = trg[edit.trg_start : edit.trg_end]

    if len(src_tokens) == 0:
        form = 'M'
    elif len(trg_tokens) == 0:
        form = 'U'
    else:
        form = 'X'

    return form

