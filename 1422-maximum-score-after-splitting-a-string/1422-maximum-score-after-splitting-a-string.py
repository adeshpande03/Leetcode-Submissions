class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        for _ in range(1, len(s)):
            m = max(m, s[:_].count('0')+s[_:].count('1'))
        return m
        