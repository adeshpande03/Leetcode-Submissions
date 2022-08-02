class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        d = {}
        for i in matrix:
            for j in i:
                if j not in d:
                    d[j] = 1
                else:
                    d[j] += 1
        del(matrix)
        s = []
        for i in d:
            for j in range(d[i]):
                s.append(i)
        s.sort()
        print(s)
        return s[k - 1]
