# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_so_far =  float('inf') * -1
#         max_ending_here = 0

#         for i in range(len(nums)):
#             max_ending_here = max_ending_here + nums[i]
#             if (max_so_far < max_ending_here):
#                 max_so_far = max_ending_here

#             if max_ending_here < 0:
#                 max_ending_here = 0
#         return max_so_far

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soFar = float('inf') * -1
        endHere = 0
        for i in nums:
            endHere = endHere + i
            if endHere > soFar:
                soFar = endHere
            if endHere < 0:
                endHere = 0
        return soFar