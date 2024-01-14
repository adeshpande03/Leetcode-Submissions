class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_total = nums[0]
        i = 0
        N = len(nums)
        while i < N - 1 and nums[i + 1] - nums[i] == 1:
            prefix_total += nums[i + 1]
            i += 1

        while True:
            if prefix_total not in nums:
                return prefix_total
            prefix_total += 1