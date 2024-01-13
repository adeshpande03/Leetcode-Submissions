class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        k = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                k+= 1
            else:
                i += 1
        print(k)        