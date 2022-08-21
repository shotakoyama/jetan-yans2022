from prettytable import PrettyTable

def calc_prf(tp, fp, fn):

    # precision
    if (tp + fp) == 0:
        p = 1.0
    else:
        p = tp / (tp + fp)

    # recall
    if (tp + fn) == 0:
        r = 0.0
    else:
        r = tp / (tp + fn)

    # F 0.5
    if (p + r) == 0:
        f = 0.0
    else:
        f = 2 * p * r / (p + r)

    return p, r, f


def format_prf(tp, fp, fn):
    p, r, f = calc_prf(tp, fp, fn)
    p = '{:.2f}'.format(p * 100)
    r = '{:.2f}'.format(r * 100)
    f = '{:.2f}'.format(f * 100)
    return p, r, f


def get_score_row(label, tp, fp, fn):
    p, r, f = format_prf(tp, fp, fn)
    return [label, tp, fp, fn, p, r, f]


def show_scorer(scorer):
    header = ['TP', 'FP', 'FN', 'Prec', 'Rec', 'F_0.5']
    table = PrettyTable([scorer.attr.title] + header)
    lst = get_score_row('score', scorer.tp, scorer.fp, scorer.fn)
    table.add_row(lst)
    print(table)


def show_type_scorer(scorer):
    header = ['TP', 'FP', 'FN', 'Prec', 'Rec', 'F_0.5']
    table = PrettyTable([scorer.attr.title] + header)

    table.align[scorer.attr.title] = 'l'
    for x in header:
        table.align[x] = 'r'

    for i, label in enumerate(scorer.attr.labels):
        lst = get_score_row(label, *scorer.array[i].tolist())
        table.add_row(lst)

    all_lst = get_score_row(
            'all',
            *scorer.array.sum(axis = 0).tolist())
    table.add_row(all_lst)

    print(table)


def show_cm_scorer(scorer):
    header = scorer.attr.labels + ['all']
    table = PrettyTable([scorer.attr.title] + header)

    table.align[scorer.attr.title] = 'l'
    for x in header:
        table.align[x] = 'r'

    for label, row in zip(scorer.attr.labels, scorer.cm):
        lst = [label] + row.tolist() + [sum(row.tolist())]
        table.add_row(lst)

    all_lst = scorer.cm.sum(axis = 0).tolist()
    table.add_row(['all'] + all_lst + [sum(all_lst)])

    print(table)

