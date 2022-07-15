from jetan.check.main import check_main

def check(first):

    def command(args):
        check_main()

    parser = first.add_parser('check')
    parser.set_defaults(handler = command)

