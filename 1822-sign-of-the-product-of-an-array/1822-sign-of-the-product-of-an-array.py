class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        n = 0
        for i in nums:
            if i < 0:
                n += 1
        return 1 if (n % 2) == 0 else -1
        