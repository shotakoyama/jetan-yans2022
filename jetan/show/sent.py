from prettytable import PrettyTable
from .word import Row

class Table:

    col_list = [
        'index',
        'text',
        'tag1',
        'tag2',
        'tag3',
        'tag4',
        'pos',
        'dep',
        'head',
        'lemma',
        'norm',
        'bi',
        'ner',
        'iob',
        'yomi',
        'kata',
        'gyogo',
        'infl',
        'onbin',
        'front',
        'deps']

    def __init__(self, sent):

        self.row_list = [
            Row(token)
            for token
            in sent]

    def __call__(self):
        table = PrettyTable(self.col_list)
        for row in self.row_list:
            table.add_row(row())
        return str(table)

