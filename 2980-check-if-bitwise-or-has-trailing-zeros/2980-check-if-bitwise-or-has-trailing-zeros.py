class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        nums = sum(map(lambda x: x%2 == 0, nums))
        print(nums)
        return nums >= 2