class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            l = max(c:=(str(i))) * len(c)
            a += int(l)
        return a

