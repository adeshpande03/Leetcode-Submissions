class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
            ans = 0
            s = set(nums)
            for i in range(len(nums)):
                j = nums[i] - diff
                k = diff + nums[i] 
                if j in s and k in s:
                    ans +=1
            return ans