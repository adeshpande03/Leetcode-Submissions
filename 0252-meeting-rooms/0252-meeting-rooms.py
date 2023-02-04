class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x:x[0])
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] < cur[-1]:
                return False
            else:
                cur = i
        return True
        