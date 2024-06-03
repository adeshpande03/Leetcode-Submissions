class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def lcs(x,y):
            ans = []
            while x and y:
                if x[0] == y[0]:
                    ans.append(x.pop(0))
                    y.pop(0)
                elif x[0] < y[0]:
                    x.pop(0)
                elif y[0] < x[0]:
                    y.pop(0)
            return ans
        
        return reduce(lambda x,y: lcs(x,y), arrays)