import sys
import json
from .token_dist import TokenDist
from .align import Aligner
from jetan.util.corr import Corr
from jetan.jet.data import JetData


def make_corr(dist, line):
    corr = Corr.decode(json.loads(line))
    aligner = Aligner(dist, corr)
    corr = aligner.make_jet_corr()
    return corr


def align_main():
    dist = TokenDist()

    corrs = [
        make_corr(dist, line)
        for index, line
        in enumerate(sys.stdin, start = 1)]
    jet_data = JetData(corrs)

    print(jet_data.encode())

