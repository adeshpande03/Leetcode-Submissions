class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums)<3:
            return nums[-1]
        return list(sorted(nums))[-3]