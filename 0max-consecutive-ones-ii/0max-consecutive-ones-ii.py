class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0 
        right = 0 
        r = 0 
        nz = 0 
        
        while right < len(nums):
            if nums[right] == 0:
                nz += 1
                
            while nz == 2:
                if nums[left] == 0:
                    nz -= 1
                left += 1
            r = max(r, right - left + 1)
            right += 1
        return r
                