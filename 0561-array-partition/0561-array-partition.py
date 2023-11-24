class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print([(nums[d], nums[d + 1]) for d in range(0, len(nums), 2)])
        return sum([min(i) for i in [(nums[d], nums[d + 1]) for d in range(0, len(nums), 2)]])
    