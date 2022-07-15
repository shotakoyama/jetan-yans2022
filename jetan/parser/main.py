from argparse import ArgumentParser
from .prepare import prepare
from .preproc import preproc
from .align import align
from .check import check
from .estimate import estimate
from .show import show
from .progress import progress
from .stat import stat

def parse_args():
    parser = ArgumentParser()
    first = parser.add_subparsers()

    prepare(first)
    preproc(first)
    align(first)
    check(first)
    estimate(first)
    show(first)

    progress(first)
    stat(first)

    return parser.parse_args()

