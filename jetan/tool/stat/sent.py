import sys
import numpy as np
from collections import defaultdict

def make_len_array(c):
    len_list = []
    for line in sys.stdin:
        if c:
            length = len(line.strip())
        else:
            length = len(line.strip().split())
        len_list.append(length)
    len_array = np.array(len_list)
    return len_array


def show_max_min(arr):
    maximum = arr.max()
    minimum = arr.min()
    print('max: {}'.format(maximum))
    print('min: {}'.format(minimum))


def show_var_std(arr):
    var = arr.var()
    std = arr.std()
    print('var: {}'.format(var))
    print('std: {}'.format(std))


def show_avg(arr):
    avg = np.mean(arr)
    print('avg: {}'.format(avg))


def show_q(arr):
    width = 10
    q_index = list(range(width, 100, width))
    q_list = np.percentile(arr, q_index)
    for index, q in zip(q_index, q_list):
        print('q{}: {}'.format(index, q))


def sent_main(c):
    len_array = make_len_array(c)
    show_max_min(len_array)
    show_var_std(len_array)
    show_avg(len_array)
    show_q(len_array)

