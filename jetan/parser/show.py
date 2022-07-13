from jetan.show.main import show_main

def show(first):

    def command(args):
        show_main()

    parser = first.add_parser('show')
    parser.set_defaults(handler = command)

