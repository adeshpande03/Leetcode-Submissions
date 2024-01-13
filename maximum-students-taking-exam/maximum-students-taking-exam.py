class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rl, cl = len(seats), len(seats[0])
        def getNextSeat(x,y):
            return (x, y + 1) if y < cl - 1 else (x + 1, 0)
        def transform(mask):
            ans = 0
            for i in range(cl, 2 * cl):
                if mask & 1 << i:
                    ans |= 1 << (i - cl)
            return ans
        @lru_cache(None)
        def solve(x, y, mask):
            if x == rl:
                return 0
            if not y:
                mask = transform(mask)
            nextSeatX, nextSeatY = getNextSeat(x,y)
            ans = solve(nextSeatX, nextSeatY, mask)
            if seats[x][y] == '#':
                return ans
            for d in ((0,-1),(-1,1),(-1,-1)):
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < rl and 0 <= ny < cl and mask & 1 << ((nx == x) * cl + ny):
                    break
            else:
                ans = max(ans, solve(nextSeatX, nextSeatY, mask | 1 << (cl + y)) + 1)
            return ans
        return solve(0,0,0)