from jetan.parser.main import parse_args

def main():
    args = parse_args()
    args.handler(args)

