class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_vals = [0]+list(accumulate(nums))
        left = 0
        for right in range(1, len(sum_vals)):
            mid = (right+left)//2
            val = (sum_vals[right]-sum_vals[mid]) - (right-mid)*nums[mid]
            val += (mid-left)*nums[mid] - (sum_vals[mid]-sum_vals[left])
            if val > k:
                left += 1
        return right-left