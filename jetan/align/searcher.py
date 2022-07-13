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
        edit = (0, 0, self.y - 1, self.y)
        self.y = self.y - 1
        return edit

    def move_leftside(self):
        edit = (self.x - 1, self.x, 0, 0)
        self.x = self.x - 1
        return edit

    def move_match(self):
        self.x = self.x - 1
        self.y = self.y - 1
        return None

    def move_diag(self):
        edit = (self.x - 1, self.x, self.y - 1, self.y)
        self.x = self.x - 1
        self.y = self.y - 1
        return edit

    def move_up(self):
        edit = (self.x - 1, self.x, self.y, self.y)
        self.x = self.x - 1
        return edit

    def move_left(self):
        edit = (self.x, self.x, self.y - 1, self.y)
        self.y = self.y - 1
        return edit

    def move_inside(self):
        now = self.array[self.x, self.y]
        up = self.array[self.x - 1, self.y]
        left = self.array[self.x, self.y - 1]
        diag = self.array[self.x - 1, self.y - 1]

        min_dist = min(up, left, diag)

        if min_dist == now == diag:
            edit = self.move_match()
        elif min_dist == diag:
            edit = self.move_diag()
        elif min_dist == up:
            edit = self.move_up()
        else:
            edit = self.move_left()

        return edit

    def move(self):
        if self.x == 0:
            edit = self.move_upside()
        elif self.y == 0:
            edit = self.move_leftside()
        else:
            edit = self.move_inside()
        return edit

