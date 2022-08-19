from prettytable import PrettyTable

def calc_prf(tp, fp, fn):
    if (tp + fp) == 0:
        p = 1.0
    else:
        p = tp / (tp + fp)

    if (tp + fn) == 0:
        r = 0.0
    else:
        r = tp / (tp + fn)

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


def show_scorer(scorer):
    p, r, f = format_prf(
            scorer.tp,
            scorer.fp,
            scorer.fn)

    table = PrettyTable([scorer.title, 'Prec', 'Rec', 'F_0.5'])
    table.add_row(['score', p, r, f])
    print(table)


def get_score_row(label, tp, fp, fn):
    p, r, f = format_prf(tp, fp, fn)
    return [label, tp, fp, fn, p, r, f]


def show_type_scorer(scorer):
    header = ['TP', 'FP', 'FN', 'Prec', 'Rec', 'F_0.5']
    table = PrettyTable([scorer.title] + header)

    table.align[scorer.title] = 'l'
    for x in header:
        table.align[x] = 'r'

    for i, label in enumerate(scorer.labels):
        lst = get_score_row(label, *scorer.cm[i].tolist())
        table.add_row(lst)

    all_lst = get_score_row(
            'all',
            *scorer.cm.sum(axis = 0).tolist())

    print(table)

