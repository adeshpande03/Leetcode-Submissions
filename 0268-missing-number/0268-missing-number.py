class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        tria = max(nums) * (max(nums)  + 1) /2
        for i in nums:
            total += i
        if nums[0] != 0:
            return 0
        if len(nums) == 1 and nums[0] != 0:
            return nums[0] - 1
        if tria == total:
            return nums[-1] + 1
        return (int(tria - total))
                