class SelectList(list):

    def min_sup(self, init_min):
        min_tmp = init_min
        for i, xs in enumerate(self):
            self[i] = [x for x in xs if x >= min_tmp]
            min_tmp = min(self[i])

    def max_sup(self, init_max):
        max_tmp = init_max
        for i, xs in list(enumerate(self))[::-1]:
            self[i] = [x for x in xs if x <= max_tmp]
            max_tmp = max(self[i])

    def min_max_sup(self, init_min = 0, init_max = 1000000):
        self.min_sup(init_min = init_min)
        self.max_sup(init_max = init_max)

    def select_top(self):
        for i, xs in enumerate(self):
            self[i] = xs[0]

