class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
            ans = 0
            for i in range(len(nums)):
                j = nums[i] - diff
                k = diff + nums[i] 
                if j in nums and k in nums:
                    ans +=1
            return ans