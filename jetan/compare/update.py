def update_corr(scorer, corr):
    for dct in corr:
        ref_edits = dct['ref']
        hyp_edits = dct['hyp']
        scorer.update_pair(ref_edits, hyp_edits)


def update_score(scorer, data):
    for corr in data:
        update_corr(scorer, corr)


def update_count(
        scorer,
        ref_edits,
        hyp_edits,
        converter = None):

    if converter is not None:
        ref_edits = converter(ref_edits)
        hyp_edits = converter(hyp_edits)

    scorer.tp += len(ref_edits & hyp_edits)
    scorer.fp += len(hyp_edits - ref_edits)
    scorer.fn += len(ref_edits - hyp_edits)


def update_type_count(
        scorer,
        ref_edits,
        hyp_edits,
        converter = None):

    if converter is not None:
        ref_edits = converter(ref_edits)
        hyp_edits = converter(hyp_edits)

    tp = ref_edits & hyp_edits
    fp = hyp_edits - ref_edits
    fn = ref_edits - hyp_edits

    for x in tp:
        scorer.update_one(x, 0)

    for x in fp:
        scorer.update_one(x, 1)

    for x in fn:
        scorer.update_one(x, 2)

