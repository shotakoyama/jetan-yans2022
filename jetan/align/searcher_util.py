from .edit import (
        NoopEdit,
        ReplaceEdit,
        UnnecessaryEdit,
        MissingEdit)

def move_upside(searcher):
    edit = MissingEdit(
            0,
            0,
            searcher.y - 1,
            searcher.y)

    searcher.y = searcher.y - 1
    return edit


def move_leftside(searcher):
    edit = UnnecessaryEdit(
            searcher.x - 1,
            searcher.x,
            0,
            0)

    searcher.x = searcher.x - 1
    return edit


def move_match(searcher):
    edit = NoopEdit(
            searcher.x - 1,
            searcher.x,
            searcher.y - 1,
            searcher.y)

    searcher.x = searcher.x - 1
    searcher.y = searcher.y - 1
    return edit


def move_diag(searcher):
    edit = ReplaceEdit(
            searcher.x - 1,
            searcher.x,
            searcher.y - 1,
            searcher.y)

    searcher.x = searcher.x - 1
    searcher.y = searcher.y - 1
    return edit


def move_up(searcher):
    edit = UnnecessaryEdit(
            searcher.x - 1,
            searcher.x,
            searcher.y,
            searcher.y)

    searcher.x = searcher.x - 1
    return edit


def move_left(searcher):
    edit = MissingEdit(
            searcher.x,
            searcher.x,
            searcher.y - 1,
            searcher.y)

    searcher.y = searcher.y - 1
    return edit

