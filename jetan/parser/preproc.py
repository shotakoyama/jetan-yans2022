from jetan.preproc.main import preproc_main

def preproc(first):

    def comamnd(args):
        preproc_main(args.name, args.mode)

    parser = first.add_parser('preproc')
    parser.add_argument(
            '-n',
            '--name',
            dest = 'name',
            default = 'ja_ginza')
    parser.add_argument(
            '-m',
            '--mode',
            dest = 'mode',
            default = 'C')
    parser.set_defaults(handler = comamnd)

