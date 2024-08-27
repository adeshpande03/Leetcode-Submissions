class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = diff = ans = 0
        for n in nums:
            ans = max(ans, diff * n)
            diff = max(diff, prefix - n)
            prefix = max(prefix, n)
        return ans
        