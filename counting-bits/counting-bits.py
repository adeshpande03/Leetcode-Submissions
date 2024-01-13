class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            c=0
            x=bin(i)
            for j in str(x):
                if j=='1': 
                    c+=1
            l.append(c)
        return l            
        