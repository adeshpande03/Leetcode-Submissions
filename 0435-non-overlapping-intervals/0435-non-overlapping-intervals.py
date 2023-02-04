class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] < cur[-1]:
                res += 1
                cur = i if i[1] < cur[1] else cur
            else:
                cur = i
        return res