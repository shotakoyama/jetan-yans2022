from .edit import Edit

class Searcher:

    def __init__(self, array):
        self.array = array
        self.src = self.array.src
        self.trg = self.array.trg
        self.x = len(self.src)
        self.y = len(self.trg)

    def is_origin(self):
        return (self.x, self.y) == (0, 0)

    def move_upside(self):
        edit = Edit(0, 0, self.y - 1, self.y)
        self.y = self.y - 1
        return edit

    def move_leftside(self):
        edit = Edit(self.x - 1, self.x, 0, 0)
        self.x = self.x - 1
        return edit

    def move_match(self):
        self.x = self.x - 1
        self.y = self.y - 1
        return None

    def move_diag(self):
        edit = Edit(self.x - 1, self.x, self.y - 1, self.y)
        self.x = self.x - 1
        self.y = self.y - 1
        return edit

    def move_up(self):
        edit = Edit(self.x - 1, self.x, self.y, self.y)
        self.x = self.x - 1
        return edit

    def move_left(self):
        edit = Edit(self.x, self.x, self.y - 1, self.y)
        self.y = self.y - 1
        return edit

    def move_inside(self):
        op = self.array.o_array[self.x, self.y]
        if op == 'N':
            edit = self.move_match()
        elif op == 'R':
            edit = self.move_diag()
        elif op == 'U':
            edit = self.move_up()
        elif op == 'M':
            edit = self.move_left()
        else:
            assert False
        return edit

    def move(self):
        if self.x == 0:
            edit = self.move_upside()
        elif self.y == 0:
            edit = self.move_leftside()
        else:
            edit = self.move_inside()
        return edit

