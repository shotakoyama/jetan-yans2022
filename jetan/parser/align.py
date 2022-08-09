from jetan.align.merge import merge_main
from jetan.align.select import select_main

def merge(second):

    def command(args):
        merge_main()

    parser = second.add_parser('merge')
    parser.set_defaults(handler = command)


def select(second):

    def command(args):
        select_main()

    parser = second.add_parser('select')
    parser.set_defaults(handler = command)


def align(first):
    parser = first.add_parser('align')
    second = parser.add_subparsers()

    merge(second)
    select(second)

