class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        s1, s2 = sum(batteries[:-n]), batteries[-n:]
        for i in range(n-1):
            s = (i+1)*(s2[i+1]-s2[i])
            if s1 >= s:
                s1 -= s
                continue
            return s2[i] + s1//(i+1)
        return s2[-1] + s1//n