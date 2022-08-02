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
        s = ''
        for i in d:
            s += (str(i) + ' ') * d[i] 
        s = s.split(' ')
        s.pop()
        s[:] = [int(d) for d in s]
        s.sort()
        print(s)
        return s[k - 1]
