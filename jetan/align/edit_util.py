from .searcher import Searcher

def make_edit_list(arr):
    searcher = Searcher(arr)
    edit_list = []

    while not searcher.is_origin():
        edit = searcher.move()
        if edit is not None:
            edit_list = [edit] + edit_list

    return edit_list


def trg_bunsetu_cond(arr, edit):
    if edit.trg_start == len(arr.trg):
        return False
    if edit.trg_start == edit.trg_end:
        return True
    return arr.trg[edit.trg_start].bunsetu == 'B'


def trg_function_word_cond(arr, edit):
    if edit.trg_start == len(arr.trg):
        return False
    if edit.trg_start == edit.trg_end:
        return True
    return arr.trg[edit.trg_start].tag1 in {'助詞', '助動詞'}


def mergeable(arr, edit1, edit2):
    if not edit1.comes_just_before(edit2):
        return False

    if trg_bunsetu_cond(arr, edit2):
        return False

    if arr.trg[edit2.trg_start].dep == 'fixed':
        return True

    if trg_function_word_cond(arr, edit1) ^ trg_function_word_cond(arr, edit2):
        return False

    return True


def make_chunk_list(arr, edit_list):
    chunk_list = [[0]]

    for index in range(1, len(edit_list)):
        if mergeable(arr, edit_list[index - 1], edit_list[index]):
            chunk_list[-1].append(index)
        else:
            chunk_list.append([index])

    return chunk_list


def merge_chunk(edit_list, chunk_list):
    new_edit_list = []

    for chunk in chunk_list:
        edit = edit_list[chunk[0]]
        for rest in chunk[1:]:
            edit = edit + edit_list[rest]
        new_edit_list.append(edit)

    return new_edit_list


def merge_edits(arr, edit_list):

    if len(edit_list) == 0:
        return []

    chunk_list = make_chunk_list(arr, edit_list)
    edit_list = merge_chunk(edit_list, chunk_list)
    return edit_list

