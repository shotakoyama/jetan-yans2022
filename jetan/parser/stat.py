from jetan.tool.stat.char import char_main
from jetan.tool.stat.sent import sent_main
from jetan.tool.stat.dist import dist_main

def char(second):

    def command(args):
        char_main(args.sort_by_freq)

    parser = second.add_parser('char')
    parser.add_argument(
            '-f',
            '--sort-by-freq',
            action = 'store_true')
    parser.set_defaults(handler = command)


def sent(second):

    def command(args):
        sent_main(args.c)

    parser = second.add_parser('sent')
    parser.add_argument(
            '-c',
            action = 'store_true')
    parser.set_defaults(handler = command)


def dist(second):

    def command(args):
        dist_main()

    parser = second.add_parser('dist')
    parser.set_defaults(handler = command)


def stat(first):
    parser = first.add_parser('stat')
    second = parser.add_subparsers()

    char(second)
    sent(second)
    dist(second)

