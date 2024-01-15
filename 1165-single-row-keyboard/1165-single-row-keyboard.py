class Solution:
    def calculateTime(self, il: str, ul: str) -> int:
        ind = 0
        c = 0
        for i in ul:
            c += abs(il.index(i) - ind)
            ind = il.index(i)
        return c
            
            
        
        