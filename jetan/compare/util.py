from pathlib import Path
from jetan.jet.data import JetData

def read_data(reference, hypothesis):
    ref_path = Path(reference).resolve()
    hyp_path = Path(hypothesis).resolve()

    with open(ref_path) as f:
        ref_data = JetData.decode(f.read())

    with open(hyp_path) as f:
        hyp_data = JetData.decode(f.read())

    assert len(ref_data) == len(hyp_data)

    return ref_data, hyp_data

