from .util import read_data

def show_edits(ref_edits, hyp_edits):

    ri, hi = 0, 0

    while (ri < len(ref_edits)) or (hi < len(hyp_edits)):
        if ri == len(ref_edits):
            print(hyp_edits[hi].encode('* H'))
            hi = hi + 1
        elif hi == len(hyp_edits):
            print(ref_edits[ri].encode('* R'))
            ri = ri + 1
        elif ref_edits[ri].span_eq(hyp_edits[hi]):
            print(ref_edits[ri].encode('  R'))
            print(hyp_edits[hi].encode('  H'))
            ri, hi = ri + 1, hi + 1
        elif ref_edits[ri].span_lt(hyp_edits[hi]):
            print(ref_edits[ri].encode('* R'))
            ri = ri + 1
        else:
            print(hyp_edits[hi].encode('* H'))
            hi = hi + 1


def analyze_main(reference, hypothesis):
    ref_data, hyp_data = read_data(reference, hypothesis)

    corr_iter = enumerate(zip(ref_data, hyp_data), start = 1)
    for corr_index, (ref_corr, hyp_corr) in corr_iter:
        print('# {}'.format(corr_index))
        print('S: ' + ref_corr.src)

        for trg_index in range(1, len(ref_corr.trgs) + 1):
            print('C: ' + ref_corr.trgs[trg_index - 1])
            ref_edits = [edit for edit in ref_corr.edits if edit.index == trg_index]
            hyp_edits = [edit for edit in hyp_corr.edits if edit.index == trg_index]
            show_edits(ref_edits, hyp_edits)


