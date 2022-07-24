from jetan.check.main import check_main

def check(first):

    def command(args):
        check_main(bar = args.bar)

    parser = first.add_parser('check')
    parser.add_argument(
            '-b',
            '--bar',
            '--progress-bar',
            dest = 'bar',
            action = 'store_true')
    parser.set_defaults(handler = command)

