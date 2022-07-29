from jetan.tool.head import head_main

def head(first):

    def command(args):
        head_main(args.n)

    parser = first.add_parser('head')
    parser.add_argument(
            '-n',
            type = int,
            default = 10)
    parser.set_defaults(handler = command)

