class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=heights[:]
        d=0
        c.sort()
        for i in range(len(c)):
            if heights[i]!=c[i]:
                d+=1
        return d
        