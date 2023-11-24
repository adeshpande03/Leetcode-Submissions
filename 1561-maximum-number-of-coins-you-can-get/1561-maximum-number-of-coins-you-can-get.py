class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        c = 0
        piles.sort()
        l = len(piles) - 2
        n = len(piles)//3
        while n > 0:
            c += piles[l]
            l -=2
            n -= 1
        
        return c
