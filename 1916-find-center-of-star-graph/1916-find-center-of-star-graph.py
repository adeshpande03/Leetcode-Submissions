class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0][0]
        b = edges[0][1]
        acount = 0
        for i in edges:
            if a in i:
                acount += 1
        if acount == len(edges):
            return a
        else:
            return b
            
        