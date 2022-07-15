from functools import lru_cache

@lru_cache(maxsize = 4096)
def char_dist(text1, text2):

    if not text1:
        return len(text2)

    if not text2:
        return len(text1)

    if text1[0] == text2[0]:
        return char_dist(text1[1:], text2[1:])

    dist = min(
            char_dist(text1, text2[1:]),
            char_dist(text1[1:], text2),
            char_dist(text1[1:], text2[1:]))

    return 1 + dist

