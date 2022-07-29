from .util import read_data
from .edit import CompEdit
from .scorer import (
        Scorer,
        FormScorer,
        UnitScorer)

def get_edits(corr, trg_index):
    offset = 0
    lst = []
    for edit in corr.edits:
        if edit.index == trg_index:
            ce = CompEdit(edit, offset)
            lst.append(ce)
            offset = offset + len(edit.text) - (edit.end - edit.start)
    return lst


def compare_main(
        reference,
        hypothesis,
        verbose = False):

    ref_data, hyp_data = read_data(reference, hypothesis)

    scorer = Scorer()
    form_scorer = FormScorer()
    unit_scorer = UnitScorer()

    corr_iter = enumerate(zip(ref_data, hyp_data), start = 1)
    for corr_index, (ref_corr, hyp_corr) in corr_iter:

        assert len(ref_corr.trgs) == len(hyp_corr.trgs)

        for trg_index in range(1, len(ref_corr.trgs) + 1):
            ref_edits = get_edits(ref_corr, trg_index)
            hyp_edits = get_edits(hyp_corr, trg_index)
            scorer.update(ref_edits, hyp_edits)
            form_scorer.update(ref_edits, hyp_edits)
            unit_scorer.update(ref_edits, hyp_edits)

        if verbose:
            print('# {}'.format(corr_index))
            scorer.show()

    print('# summary')
    scorer.show()
    form_scorer.show()
    unit_scorer.show()

