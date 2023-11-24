class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, max(candies)
        while l <= r:
            m = (l+r)//2
            l, r = (m+1, r) if not m or sum(candy // m for candy in candies) >= k else (l, m-1)
        return r