class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(map(int, list(''.join(list(map(str, nums))))))