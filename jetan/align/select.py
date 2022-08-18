import sys
import json
from .token_dist import TokenDist
from .dist_array import DistArray
from jetan.util.corr import Corr
from jetan.jet.edit import JetEdit
from jetan.jet.corr import JetCorr
from jetan.jet.data import JetData
from .searcher import Searcher
from .start_list import StartList
from .end_list import EndList
from functools import reduce

def split_edit_list(edit_list, start_list, end_list):
    assert len(edit_list) == len(start_list) == len(end_list)

    span_list = list(zip(start_list, end_list))
    block_list = []

    tmp = None
    for span, edit in zip(span_list, edit_list):
        if tmp is None or tmp != span:
            block_list.append([edit])
        else:
            block_list[-1].append(edit)
        tmp = span

    return block_list


def get_source_start_end(corr, edit):
    ss = edit.src_start
    se = edit.src_end

    if ss < len(corr.src):
        start = corr.src[ss].front
    else:
        start = len(str(corr.src))

    if se < len(corr.src):
        end = corr.src[se].front
    else:
        end = len(str(corr.src))

    return start, end


def make_corr(dist, line):
    corr = Corr.decode(json.loads(line))
    src_spans = corr.src.get_bunsetu_spans()

    edits = []

    for anno_index, trg in enumerate(corr.trgs, start = 1):
        arr = DistArray(dist, corr.src, trg)
        searcher = Searcher(arr)
        edit_list = searcher.search()

        start_list = StartList(corr, trg, edit_list)
        start_list.make()

        end_list = EndList(corr, trg, edit_list, start_list)
        end_list.make()

        block_list = split_edit_list(edit_list, start_list, end_list)

        for block in block_list:
            if any(edit.form != 'N' for edit in block):
                edit = reduce(lambda x, y: x + y, block)
                src_start, src_end = get_source_start_end(corr, edit)
                jet_edit = JetEdit(
                        anno_index,
                        src_start,
                        src_end,
                        'X',
                        'Y',
                        ''.join([
                            x.text
                            for x
                            in trg[edit.trg_start : edit.trg_end]]))
                edits.append(jet_edit)

    src = str(corr.src)
    trgs = [str(trg) for trg in corr.trgs]
    return JetCorr(src, trgs, edits)


def select_main():
    dist = TokenDist()

    corrs = [
        make_corr(dist, line)
        for index, line
        in enumerate(sys.stdin, start = 1)]

    jet_data = JetData(corrs)
    print(jet_data.encode())

