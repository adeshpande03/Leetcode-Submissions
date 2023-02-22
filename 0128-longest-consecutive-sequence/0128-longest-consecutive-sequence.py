class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        nums = list(set(nums))
        nums.sort()
        nums.append(math.inf)
        
        maxMum = 0
        tempCount = 0
        prevNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prevNum == 1:
                tempCount += 1
            else:
                if tempCount > maxMum:
                    maxMum = tempCount
                tempCount = 0
            prevNum = nums[i]
        return maxMum + 1