class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dl=[]
        for i in dimensions:
            temp=i[0]*i[0]+i[1]*i[1]
            dl.append(((temp)))
        maxe=max(dl)
        res=[]
        for i in range(len(dl)):
            if dl[i]==maxe:
                res.append(dimensions[i][0]*dimensions[i][1])
        return max(res)