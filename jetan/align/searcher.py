from .searcher_util import (
        move_upside,
        move_leftside,
        move_match,
        move_diag,
        move_up,
        move_left)

class Searcher:

    def __init__(self, array):
        self.array = array
        self.src = self.array.src
        self.trg = self.array.trg
        self.x = len(self.src)
        self.y = len(self.trg)

    def is_origin(self):
        return (self.x, self.y) == (0, 0)

    def move_inside(self):
        op = self.array.o_array[self.x, self.y]

        if op == 'N':
            edit = move_match(self)
        elif op == 'R':
            edit = move_diag(self)
        elif op == 'U':
            edit = move_up(self)
        elif op == 'M':
            edit = move_left(self)
        else:
            assert False
        return edit

    def move(self):
        if self.x == 0:
            edit = move_upside(self)
        elif self.y == 0:
            edit = move_leftside(self)
        else:
            edit = self.move_inside()
        return edit

    def search(self):
        edit_list = []

        while not self.is_origin():
            edit = self.move()
            edit_list = [edit] + edit_list

        return edit_list

