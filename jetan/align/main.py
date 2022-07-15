import sys
import json
from itertools import product
import numpy as np
from .token_dist import TokenDist
from .align import Aligner
from jetan.util.corr import Corr

def align_main():
    dist = TokenDist()

    for index, line in enumerate(sys.stdin, start = 1):
        corr = Corr.decode(json.loads(line))
        aligner = Aligner(dist, corr)

        aligner.show_header(index)
        aligner.show_source()
        aligner.show_targets()
        aligner.show_annotations()
        print()

