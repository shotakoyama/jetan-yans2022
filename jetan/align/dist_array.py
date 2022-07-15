import numpy as np

class DistArray:

    def __init__(self, dist, src, trg):
        self.dist = dist
        self.src = src
        self.trg = trg
        self.init_array()
        self.make_array()

    def init_array(self):
        self.d_array = np.empty((
            len(self.src) + 1,
            len(self.trg) + 1),
            dtype = np.float)
        self.o_array = np.empty((
            len(self.src) + 1,
            len(self.trg) + 1),
            dtype = np.unicode)

        self.d_array[0, 0] = 0
        self.o_array[0, 0] = '?'

        for x in range(1, len(self.src) + 1):
            self.d_array[x, 0] = self.d_array[x - 1, 0] + self.dist.del_dist(self.src[x - 1])
            self.o_array[x, 0] = '?'

        for y in range(1, len(self.trg) + 1):
            self.d_array[0, y] = self.d_array[0, y - 1] + self.dist.ins_dist(self.trg[y - 1])
            self.o_array[0, y] = '?'

    def fill_array_noop(self, x, y):
        self.d_array[x, y] = self.d_array[x - 1, y - 1]
        self.o_array[x, y] = 'N'

    def fill_array_op(self, x, y):
        s = self.d_array[x - 1, y - 1] + self.dist.sub_dist(self.src[x - 1], self.trg[y - 1])
        d = self.d_array[x - 1, y] + self.dist.del_dist(self.src[x - 1])
        i = self.d_array[x, y - 1] + self.dist.ins_dist(self.trg[y - 1])
        a, b = min((s, 'R'), (d, 'U'), (i, 'M'), key = lambda x: x[0])
        self.d_array[x, y] = a
        self.o_array[x, y] = b

    def fill_array(self, x, y):
        if self.src[x - 1].text == self.trg[y - 1].text:
            self.fill_array_noop(x, y)
        else:
            self.fill_array_op(x, y)

    def make_array(self):
        for x in range(1, len(self.src) + 1):
            for y in range(1, len(self.trg) + 1):
                self.fill_array(x, y)

