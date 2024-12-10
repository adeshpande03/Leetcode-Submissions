class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        for c in {*s}:
            q = [*map(len, nlargest(3, findall(c+'+', s))), 0, 0]
            res = max(res, q[0]-2, q[1]-(q[0]==q[1]), q[2])

        return res or -1