class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mat = list(map(sum, mat))
        m = 0
        r = 0
        for j, i in enumerate(mat):
            if i > m:
                m = i
                r = j
        return r, m
                
                