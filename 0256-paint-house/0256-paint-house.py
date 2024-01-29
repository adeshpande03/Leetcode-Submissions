from functools import cache
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dfs(i, prevColor):
            if i == len(costs): return 0
            res = float('inf')
            for color in range(3):
                if color == prevColor: continue
                res = min(res, costs[i][color]+dfs(i+1,color))
            return res
        return dfs(0, -1)
