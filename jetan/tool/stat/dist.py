import sys
import numpy as np
from tqdm import tqdm
from jetan.align.char_dist import char_dist

class Example:

    def __init__(self, line):
        line = line.strip().split('\t')

        self.src = line[0]

        assert len(line) > 0
        if len(line) == 1:
            self.trgs = [self.src]
        else:
            self.trgs = line[1:]

        self.src_len = len(self.src)
        self.trg_lens = [len(trg) for trg in self.trgs]
        self.dists = [char_dist(self.src, trg) for trg in self.trgs]

    def avg_dist(self):
        return np.mean(self.dists)

    def avg_dist_ratio(self):
        lst = [
            dist / max(self.src_len, trg_len)
            for trg_len, dist
            in zip(self.trg_lens, self.dists)]
        return np.mean(lst)


def dist_main():

    examples = [
            Example(line)
            for line
            in tqdm(sys.stdin)]
    print('{} examples'.format(len(examples)))

    avg_dist = np.mean([example.avg_dist() for example in examples])
    print('avg char dist: {:.2f}'.format(avg_dist * 100))

    dist_ratio = np.mean([example.avg_dist_ratio() for example in examples])
    print('char dist ratio: {:.2f}'.format(dist_ratio * 100))




