from .char_dist import char_dist

class TokenDist:

    def __init__(
            self,
            del_cost = 0.5,
            ins_cost = 0.5,
            yomi_coef = 0.5,
            lemma_coef = 0.25,
            pos_coef = 0.251):
        self.del_cost = del_cost
        self.ins_cost = ins_cost
        self.yomi_coef = yomi_coef
        self.lemma_coef = lemma_coef
        self.pos_coef = pos_coef

    def del_dist(self, token):
        return self.del_cost

    def ins_dist(self, token):
        return self.ins_cost

    def yomi_cost(self, token1, token2):
        max_len = max(
                len(token1.yomi),
                len(token2.yomi))
        dist = char_dist(token1.yomi, token2.yomi) / max_len
        return dist

    def yomi_dist(self, token1, token2):
        if (token1.yomi is None) or (token2.yomi is None):
            dist = self.yomi_coef
        else:
            dist = self.yomi_coef * self.yomi_cost(token1, token2)
        return dist

    def lemma_dist(self, token1, token2):
        if token1.lemma == token2.lemma:
            dist = 0.0
        else:
            dist = self.lemma_coef
        return dist

    def pos_dist(self, token1, token2):
        if token1.pos == token2.pos:
            dist = 0.0
        else:
            dist = self.pos_coef
        return dist

    def sub_dist(self, token1, token2):

        if token1.text == token2.text:
            dist = 0.0
        else:
            y = self.yomi_dist(token1, token2)
            l = self.lemma_dist(token1, token2)
            p = self.pos_dist(token1, token2)
            dist = y + l + p
        return dist

