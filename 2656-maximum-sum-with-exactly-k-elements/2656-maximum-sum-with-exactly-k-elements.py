class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = nums[-1]
        return p*k + k * (k - 1)//2
        