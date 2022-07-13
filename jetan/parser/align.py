from jetan.align.main import align_main

def align(first):

    def command(args):
        align_main()

    parser = first.add_parser('align')
    parser.set_defaults(handler = command)

