class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        baan = 1
        points.sort(key = lambda x: (x[0], x[1]))
        hold = points[0]
        for i in points:
            if i[0] <= hold[1]:
                hold = [i[0], min(i[1], hold[1])]
            else:
                baan += 1
                hold = i
        return baan
    

