import sys
import numpy as np
from itertools import product
from collections import defaultdict

def get_pair_list():
    line_list = [
            line.rstrip('\n').split('\t')
            for line
            in sys.stdin]

    pair_list = [
            (tup[0], trg)
            for tup in line_list
            for trg in tup[1:]]

    return pair_list


def make_array(src, trg):
    d_arr = np.zeros((len(src) + 1, len(trg) + 1), dtype = np.int)
    o_arr = np.zeros((len(src) + 1, len(trg) + 1), dtype = np.unicode)
    xy_iter = product(
            range(1, len(src) + 1),
            range(1, len(trg) + 1))
    for x, y in xy_iter:
        d_arr[x, y], o_arr[x, y] = max(
                (d_arr[x - 1, y], 'D'),
                (d_arr[x, y - 1], 'I'),
                (d_arr[x - 1, y - 1] + 1, 'M')
                if src[x - 1] == trg[y - 1] else
                (d_arr[x - 1, y - 1], 'R'))
    return d_arr, o_arr


def trace_array(arr):
    span_list = []
    x = arr.shape[0] - 1
    y = arr.shape[1] - 1
    while x > 0 and y > 0:
        if arr[x, y] == 'D':
            span_list.insert(0, (x - 1, x, y, y))
            x = x - 1
        elif arr[x, y] == 'I':
            span_list.insert(0, (x, x, y - 1, y))
            y = y - 1
        elif arr[x, y] == 'R':
            span_list.insert(0, (x - 1, x, y - 1, y))
            x, y = x - 1, y - 1
        else:
            x, y = x - 1, y - 1
    return span_list


def merge_spans(span_list):
    if len(span_list) < 2:
        return span_list

    head = span_list[0]
    tail = span_list[1:]

    if head[1] == tail[0][0] and head[3] == tail[0][2]:
        tup = (head[0], tail[0][1], head[2], tail[0][3])
        return merge_spans([tup] + tail[1:])
    else:
        return [head] + merge_spans(tail)


def get_span_list(src, trg):
    d_arr, o_arr = make_array(src, trg)
    span_list = trace_array(o_arr)
    span_list = merge_spans(span_list)
    return span_list


def get_edit_iter(src, trg):
    span_list = get_span_list(src, trg)
    for xs, xe, ys, ye in span_list:
        x = src[xs : xe]
        if x == '':
            x = '■'
        y = trg[ys : ye]
        if y == '':
            y = '■'
        yield x, y


def diff_main():
    count = defaultdict(int)

    pair_list = get_pair_list()
    for src, trg in pair_list:
        for x, y in get_edit_iter(src, trg):
            count[(x, y)] += 1

    lst = [(x, y, f) for (x, y), f in count.items()]
    lst.sort(key = lambda x: -x[2])
    for x, y, f in lst:
        print(x, y, f)

