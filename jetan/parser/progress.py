from jetan.tool.progress import progress_main

def progress(first):
    parser = first.add_parser('progress')
    parser.set_defaults(handler = lambda args: progress_main())

