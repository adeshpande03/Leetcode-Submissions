class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = '{:032b}'.format(start)
        e = '{:032b}'.format(goal)
        t = 0
        for i in range(len(s)):
            t += abs(ord(s[i]) - ord(e[i]))
        return t