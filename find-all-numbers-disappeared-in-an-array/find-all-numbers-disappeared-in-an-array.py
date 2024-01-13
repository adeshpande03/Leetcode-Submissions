class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(range(1, n + 1))
        return (list(s - set(nums)))