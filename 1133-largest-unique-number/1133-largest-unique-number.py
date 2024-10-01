class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)

        res = - 1
        for k in c:
            if c[k] == 1:
                res = max(res, k)
        
        return res