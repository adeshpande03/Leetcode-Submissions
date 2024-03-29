class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return n
        d={}
        k={}
        for i in range(1,n+1):
            d[i]=1
        for i in trust:
            if i[0] in d:
                del d[i[0]]
            if i[1] in k:
                k[i[1]]=k[i[1]]+1
            else:
                k[i[1]]=1
        if len(d)!=1:
            return -1
        for i,j in k.items():
            if j==n-1:
                return i
        return -1