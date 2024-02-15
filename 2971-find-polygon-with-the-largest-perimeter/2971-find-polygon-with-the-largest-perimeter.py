class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans=-1
        nums.sort()
        cur=nums[0]+nums[1]
        for i in range(2,len(nums)):
            if(cur>nums[i]):
                ans=cur+nums[i]
            cur+=nums[i]
        return ans