import sys
import json
from itertools import product
import numpy as np
from .token_dist import TokenDist
from .dist_array import DistArray
from .searcher import Searcher
from jetan.util.corr import Corr

def make_cost_array(dist, src, trg):
    arr = np.empty((len(src) + 1, len(trg) + 1), dtype = np.float)

    arr[0, 0] = 0

    for x in range(1, len(src) + 1):
        arr[x, 0] = dist.del_dist(src[x - 1])

    for y in range(1, len(trg) + 1):
        arr[0, y] = dist.ins_dist(trg[y - 1])

    for x, y in product(range(1, len(src) + 1), range(1, len(trg) + 1)):
        arr[x, y] = min(
            arr[x - 1, y - 1] + dist.sub_dist(src[x - 1], trg[y - 1]),
            arr[x - 1, y    ] + dist.del_dist(src[x - 1]),
            arr[x    , y - 1] + dist.ins_dist(trg[y - 1]))

    return arr


def align_main():

    dist = TokenDist()

    for index, line in enumerate(sys.stdin, start = 1):
        print('# {}'.format(index))

        corr = Corr.decode(json.loads(line))
        src = corr.src
        print('S\t{}'.format(str(src)))

        for trg in corr.trgs:
            print('C\t{}'.format(str(trg)))

        for anno_id, trg in enumerate(corr.trgs, start = 1):
            arr = DistArray(dist, src, trg)
            searcher = Searcher(arr)

            edit_list = []
            while not searcher.is_origin():
                edit = searcher.move()
                if edit is not None:
                    edit_list = [edit] + edit_list

            for ss, se, ts, te in edit_list:
                if ss < len(src):
                    start = src[ss].front
                else:
                    start = len(str(src))

                if se < len(src):
                    end = src[se].front
                else:
                    end = len(str(src))

                edit_trg = ''.join(token.text for token in trg[ts : te])

                line = '\t'.join([
                    'A',
                    str(anno_id),
                    str(start),
                    str(end),
                    edit_trg,
                    'X',
                    'Y',
                    '_'])
                print(line)
        print()




