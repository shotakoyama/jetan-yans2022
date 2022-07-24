import sys
from tqdm import tqdm
from jetan.jet.data import JetData

def check_order(index, corr):
    anno = 0
    pos = 0

    for edit in corr.edits:

        if edit.index < anno:
            line = '# {}\n'.format(index)
            line = line + '!!! Annotator ID Order Error\n'
            raise Exception(line + corr.encode())
        if edit.index > anno:
            anno = edit.index
            pos = 0

        if pos > edit.start:
            line = '# {}\n'.format(index)
            line = line + '!!! Start Position Error\n'
            raise Exception(line + corr.encode())
        if edit.start > edit.end:
            line = '# {}\n'.format(index)
            line = line + '!!! End Position Error\n'
            raise Exception(line + corr.encode())

        pos = edit.end


def edit_sent(sent, offset, start, end, text):
    sent = sent[ : start + offset] + text + sent[end + offset : ]
    diff = len(text) - (end - start)
    offset = offset + diff
    return sent, offset


def check_consistency(index, corr):
    text_list = [corr.src for _ in corr.trgs]
    offset_list = [0 for _ in corr.trgs]

    for edit in corr.edits:
        sent = text_list[edit.index - 1]
        offset = offset_list[edit.index - 1]
        sent, offset = edit_sent(sent, offset, edit.start, edit.end, edit.text)
        text_list[edit.index - 1] = sent
        offset_list[edit.index - 1] = offset

    for trg, text in zip(corr.trgs, text_list):
        if trg != text:
            line = '# {}\n'.format(index)
            line = line + '!!! Target Error\n'
            line = line + '!!! target: {}\n'.format(trg)
            line = line + '!!! edited: {}\n'.format(text)
            raise Exception(line + corr.encode())


def check_try(bar):
    data = JetData.decode(sys.stdin.read())

    iterator = enumerate(data, start = 1)
    if bar:
        iterator = tqdm(iterator, bar_format = '{l_bar}{r_bar}')

    for index, corr in iterator:
        check_order(index, corr)
        check_consistency(index, corr)


def check_main(bar):
    try:
        check_try(bar)
    except Exception as e:
        print(e)
    else:
        print('ok')

