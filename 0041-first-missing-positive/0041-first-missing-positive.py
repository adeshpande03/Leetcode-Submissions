class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c = list(range(1, 2**16))
        for i in nums:
            
            if c[i - 1] == i:
                c[i - 1] = 2**31 + 1
        return min(c)