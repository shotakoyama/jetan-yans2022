import sys
import json
from .preproc import Preproc
from jetan.util.corr import Corr

def preproc_main(
        name = 'ja_ginza',
        mode = 'C'):

    preproc = Preproc(name, mode)

    for line in sys.stdin:
        line = line.strip().split('\t')
        line = [preproc(sent) for sent in line]
        line = Corr(line[0], line[1:])
        line = line.encode()
        line = json.dumps(line, ensure_ascii = False)
        print(line)

