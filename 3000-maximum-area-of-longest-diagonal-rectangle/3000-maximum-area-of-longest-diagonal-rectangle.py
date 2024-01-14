class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        a = []
        l = 0
        for i, j in enumerate(d):
            if (j[0]**2 + j[1] **2) > l:
                a.clear()
                a.append(j[0] * j[1])
                l = j[0]**2 + j[1] **2
            elif j[0]**2 + j[1] **2 == l:
                a.append(j[0] * j[1])
        return max(a)
            