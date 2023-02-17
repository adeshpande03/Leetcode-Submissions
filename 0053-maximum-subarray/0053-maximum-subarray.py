class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soFar = float('inf') * -1
        endHere = 0
        for i in nums:
            endHere = endHere + i
            if endHere > soFar:
                soFar = endHere
            if endHere <= 0:
                endHere = 0
        return soFar