class Solution(object):
    def isBoomerang(self, p):
        x1, y1, x2, y2, x3, y3 = p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1]
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0