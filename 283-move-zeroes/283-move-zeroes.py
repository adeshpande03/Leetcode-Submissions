class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ogLen = len(nums)
        nums[:] = [d for d in nums if d != 0]
        for i in range(ogLen - len(nums)):
            nums.append(0)