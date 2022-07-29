from jetan.compare.main import compare_main

def compare(first):

    def command(args):
        compare_main(
                args.reference,
                args.hypothesis,
                args.verbose)

    parser = first.add_parser('compare')
    parser.add_argument('reference')
    parser.add_argument('hypothesis')
    parser.add_argument(
            '-v',
            '--verbose',
            dest = 'verbose',
            action = 'store_true')
    parser.set_defaults(handler = command)

