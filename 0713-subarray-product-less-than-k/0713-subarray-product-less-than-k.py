class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        
        for right, value in enumerate(nums):
            product *= value
            
            while product >= k and left < right:
                product //= nums[left]
                left += 1
                
            if product < k:
                count += right - left + 1
        return count