class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        il=[]
        il[:0] = keyboard
        ul = []
        ul[:0] = word
        
        ind = 0
        c = 0
        for i in ul:
            c += abs(il.index(i) - ind)
            ind = il.index(i)
        return c
            
            
        
        