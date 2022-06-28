from argparse import ArgumentParser
from .prepare import prepare
from .preproc import preproc
from .align import align
from .estimate import estimate

def parse_args():
    parser = ArgumentParser()
    first = parser.add_subparsers()

    prepare(first)
    preproc(first)
    align(first)
    estimate(first)

    return parser.parse_args()

