class Solution:
    def numSplits(self, s: str) -> int:
        c = Counter(s)
        d = Counter()
        ans = 0
        for i in s:
            c[i] -= 1
            d[i] += 1
            if c[i] == 0:
                del c[i]
            if len(c) == len(d):
                ans += 1
        return ans