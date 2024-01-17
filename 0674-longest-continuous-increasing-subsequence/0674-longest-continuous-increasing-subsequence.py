class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        curr_len = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr_len += 1
                ans = max(ans,curr_len)
            else:
                curr_len = 1
        return ans