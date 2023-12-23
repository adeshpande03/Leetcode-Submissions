class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        c = [0] + list(accumulate(nums.copy()))[:-1]
        d = list(accumulate(nums.copy()[::-1]))[::-1][1:] + [0]
        return [abs(c[i] - d[i]) for i in range(len(c))]