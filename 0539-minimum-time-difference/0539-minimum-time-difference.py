class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def ttom(t):
            t = t.split(":")
            h = t[0]
            m = t[1]
            return ((int(h) * 60 + int(m)) - 1440) % (24 * 60)
        c = (list(map(ttom, timePoints)))
        c.sort()
        print(c)
        m = 1440
        for i in range(len(c) - 1):
            t = c[i + 1] - c[i]
            m = min(m, t)
        m = min(m, 1440 - c[-1] + c[0])
        return m
        return 0

        