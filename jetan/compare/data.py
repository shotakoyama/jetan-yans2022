from .edit import CompEdit

def offset_diff(edit):
    return len(edit.text) - (edit.end - edit.start)


def get_edits(corr, trg_index):
    offset = 0
    lst = []
    for edit in corr.edits:
        if edit.index == trg_index:
            ce = CompEdit(edit, offset)
            lst.append(ce)
            offset = offset + offset_diff(edit)
    return lst


def make_comp_corr(ref_corr, hyp_corr):
    assert len(ref_corr.trgs) == len(hyp_corr.trgs)

    corr = [{
        'ref': get_edits(ref_corr, trg_index),
        'hyp': get_edits(hyp_corr, trg_index)}
        for trg_index
        in range(1, len(ref_corr.trgs) + 1)]
    return corr


def make_comp_data(ref_data, hyp_data):
    corr_iter = zip(ref_data, hyp_data)

    data = [
        make_comp_corr(ref_corr, hyp_corr)
        for ref_corr, hyp_corr
        in zip(ref_data, hyp_data)]

    return data

