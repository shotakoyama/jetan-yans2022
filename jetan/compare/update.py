def update_corr(scorer, corr):
    for dct in corr:
        ref_edits = dct['ref']
        hyp_edits = dct['hyp']
        scorer.update_pair(ref_edits, hyp_edits)


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

    tp = ref_edits & hyp_edits # true positive
    fp = hyp_edits - ref_edits # false positive
    fn = ref_edits - hyp_edits # false negative

    for x in tp:
        scorer.update_one(x, 0)

    for x in fp:
        scorer.update_one(x, 1)

    for x in fn:
        scorer.update_one(x, 2)


def update_cm_count(
        scorer,
        ref_edits,
        hyp_edits,
        converter = None):

    if converter is not None:
        ref_edits = converter(ref_edits)
        hyp_edits = converter(hyp_edits)

    ref_dict = {
            edit[1:]: edit[0]
            for edit
            in ref_edits}
    hyp_dict = {
            edit[1:]: edit[0]
            for edit
            in hyp_edits}
    ref_spans = set(ref_dict.keys())
    hyp_spans = set(hyp_dict.keys())
    match_spans = ref_spans & hyp_spans

    for span in match_spans:
        ref_label = ref_dict[span]
        hyp_label = hyp_dict[span]
        scorer.update_one(ref_label, hyp_label)

