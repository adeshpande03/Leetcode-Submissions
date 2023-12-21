class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [i[0] for i in points]
        points.sort()
        m = 0
        for i in range(len(points[1:])):
            m = max(m, points[i] - points[i - 1])
        return m