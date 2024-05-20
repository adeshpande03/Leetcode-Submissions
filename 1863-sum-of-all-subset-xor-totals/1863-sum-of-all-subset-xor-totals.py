class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        
        def backtrack(start,curr):
            nonlocal ans
            ans+=curr
            if start==len(nums):
                return

            for i in range(start,len(nums)):
                curr=curr^nums[i]
                backtrack(i+1,curr)
                curr = curr^nums[i]

        backtrack(0,0)
        return ans