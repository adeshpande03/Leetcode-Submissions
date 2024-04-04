class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        t = 0
        for i in s:
            if i == '(':
                t += 1
            if i == ')':
                t -= 1
            m = max(t, m)
        return m