from collections import Counter
from math import comb


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        output = 0

        for f in Counter(s).values():
            output += f + comb(f, 2)

        return output