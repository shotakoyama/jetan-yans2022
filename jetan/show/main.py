import sys
from jetan.util.decode import decode_corr
from .sent import Table

def show_main():

    for index, corr in enumerate(sys.stdin, start = 1):

        corr = decode_corr(corr)
        src_tab = Table(corr.src)

        print('# {}-0: {}'.format(index, str(corr.src)))
        print(src_tab())

        for trg_id, trg in enumerate(corr.trgs, start = 1):

            trg_tab = Table(trg)

            print('# {}-{}: {}'.format(index, trg_id, str(trg)))
            print(trg_tab())

