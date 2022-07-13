import numpy as np
from itertools import product

class DistArray:

    def __init__(self, dist, src, trg):
        self.dist = dist
        self.src = src
        self.trg = trg
        self.make_array()

    def make_array(self):
        self.array = np.empty(
                (len(self.src) + 1, len(self.trg) + 1),
                dtype = np.float)

        xs = range(1, len(self.src) + 1)
        ys = range(1, len(self.trg) + 1)

        self.array[0, 0] = 0

        for x in xs:
            self.array[x, 0] = self.dist.del_dist(self.src[x - 1])

        for y in ys:
            self.array[0, y] = self.dist.ins_dist(self.trg[y - 1])

        for x, y in product(xs, ys):
            self.array[x, y] = min(
                self.array[x - 1, y - 1]
                    + self.dist.sub_dist(
                        self.src[x - 1],
                        self.trg[y - 1]),
                self.array[x - 1, y    ]
                    + self.dist.del_dist(
                        self.src[x - 1]),
                self.array[x    , y - 1]
                    + self.dist.ins_dist(
                        self.trg[y - 1]))

    def __getitem__(self, tup):
        return self.array[tup]

