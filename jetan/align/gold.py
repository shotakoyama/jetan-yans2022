import sys
import json
from pathlib import Path
from jetan.util.corr import Corr
from jetan.jet.edit import JetEdit
from jetan.jet.corr import JetCorr
from jetan.jet.data import JetData


def get_ref_data(ref_path):
    ref_path = Path(ref_path).resolve()
    with open(ref_path) as f:
        ref_data = JetData.decode(f.read())
    return ref_data


def make_corr(line, ref_corr):
    corr = Corr.decode(json.loads(line))
    src = str(corr.src)
    trgs = [str(trg) for trg in corr.trgs]
    edits = [
        JetEdit(
            edit.index,
            edit.start,
            edit.end,
            'X',
            'Y',
            edit.text,
            edit.note)
        for edit
        in ref_corr.edits]
    corr = JetCorr(src, trgs, edits)
    return corr


def gold_main(ref_path):
    ref_data = get_ref_data(ref_path)
    corrs = [
        make_corr(line, ref_corr)
        for line, ref_corr
        in zip(sys.stdin, ref_data)]
    jet_data = JetData(corrs)
    print(jet_data.encode())

