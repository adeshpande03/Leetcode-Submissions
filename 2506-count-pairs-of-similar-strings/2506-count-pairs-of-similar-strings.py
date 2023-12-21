class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = map(tuple, map(set, words))
        c = Counter(words)
        ans = 0
        for n in c:
            ans += factorial(c[n])/(2 * factorial(c[n] - 2)) if c[n] > 1 else 0
        return int(ans)