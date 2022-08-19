from .util import read_data
from .data import make_comp_data
from .span_scorer import SpanScorer
from .full_scorer import FullScorer
from .form_scorer import FormScorer
from .unit_scorer import UnitScorer

def compare_main(
        reference,
        hypothesis,
        verbose = False):

    ref_data, hyp_data = read_data(reference, hypothesis)
    data_edits = make_comp_data(ref_data, hyp_data)

    span_scorer = SpanScorer().update(data_edits)
    span_scorer.show()

    full_scorer = FullScorer().update(data_edits)
    full_scorer.show()

    form_scorer = FormScorer().update(data_edits)
    form_scorer.show()

    unit_scorer = UnitScorer().update(data_edits)
    unit_scorer.show()

