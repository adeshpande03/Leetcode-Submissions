class Solution:
    def minimumChairs(self, s: str) -> int:
        m = -1
        c = 0
        for i in s:
            if i == 'E':
                c += 1
                m = max(m, c)
            if i == 'L':
                c -= 1
        return m
