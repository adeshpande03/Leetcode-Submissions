class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        monthdays = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        start, end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        
        start_month, start_day = int(start[:2]), int(start[3:])
        end_month, end_day = int(end[:2]), int(end[3:])
        
        if start > end: return 0
        elif start_month == end_month: 
            return end_day - start_day + 1
        else: 
            return (monthdays[start_month] - start_day) + sum([monthdays[i] for i in range(start_month + 1, end_month)]) + end_day + 1