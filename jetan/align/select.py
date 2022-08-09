import sys
import json
from .token_dist import TokenDist
from .dist_array import DistArray
from .edit_util import make_edit_list
from .align import Aligner
from jetan.util.corr import Corr
from jetan.jet.data import JetData
from .searcher import Searcher

def get_pos_lists(bunsetu_spans):
    pos_list = [
            index
            for index, (start, end)
            in enumerate(bunsetu_spans)
            for _
            in range(start, end)]
    start_pos = pos_list + [pos_list[-1]]
    end_pos = [pos_list[0]] + pos_list
    return start_pos, end_pos


def get_spans(src, trg, edit_list, bunsetu_spans):
    print(src)
    print(trg)
    print(edit_list)
    print(bunsetu_spans)

    bunsetu_edit_list = [
            list()
            for span
            in bunsetu_spans]
    start_pos, end_pos = get_pos_lists(bunsetu_spans)

    for edit in edit_list:
        start_bunsetu = start_pos[edit.trg_start]
        end_bunsetu = end_pos[edit.trg_end]
        assert start_bunsetu == end_bunsetu, (str(trg), start_bunsetu, end_bunsetu, edit.trg_start, edit.src_start, trg[edit.trg_start].text)



    #for edit in edit_list:
    #    print(edit)
    #print(bunsetu_edit_list)


def select_main():
    dist = TokenDist()

    for index, line in enumerate(sys.stdin, start = 1):
        corr = Corr.decode(json.loads(line))
        for anno_id, trg in enumerate(corr.trgs, start = 1):
            arr = DistArray(dist, corr.src, trg)
            searcher = Searcher(arr)
            edit_list = searcher.search()

            src_spans = corr.src.get_bunsetu_spans()
            trg_spans = trg.get_bunsetu_spans()
            print('---')
            print(src_spans)
            print(trg_spans)

