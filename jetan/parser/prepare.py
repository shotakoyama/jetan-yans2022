from jetan.prepare.naist import naist_main

def naist(second):
    parser = second.add_parser('naist')
    parser.add_argument('base')
    parser.set_defaults(handler = lambda args: naist_main(args.base))


def prepare(first):
    parser = first.add_parser('prepare')
    second = parser.add_subparsers()

    naist(second)

