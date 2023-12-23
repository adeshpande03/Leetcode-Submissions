class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = set()
        seen.add((x, y))
        d = {"N":(1, 0),"E":(0, 1),"S":(-1, 0),"W":(0, -1)}
        for i in path:
            x += d[i][1]
            y += d[i][0]
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False