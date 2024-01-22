class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks.sort()
        c = 0
        while len(sticks) != 1:
            s = sticks[0] + sticks[1]
            sticks = sticks[2:]
            insort(sticks, s)
            c += s
        return c