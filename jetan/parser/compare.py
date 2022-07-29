from jetan.compare.main import compare_main
from jetan.compare.analyze import analyze_main

def compare(first):

    def command(args):
        if args.analyze:
            analyze_main(
                    args.reference,
                    args.hypothesis)
        else:
            compare_main(
                    args.reference,
                    args.hypothesis,
                    args.verbose)

    parser = first.add_parser('compare')
    parser.add_argument('reference')
    parser.add_argument('hypothesis')
    parser.add_argument(
            '-a',
            '--analyze',
            dest = 'analyze',
            action = 'store_true')
    parser.add_argument(
            '-v',
            '--verbose',
            dest = 'verbose',
            action = 'store_true')
    parser.set_defaults(handler = command)

