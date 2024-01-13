class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for d in map(len, map(str, nums)) if not d% 2])