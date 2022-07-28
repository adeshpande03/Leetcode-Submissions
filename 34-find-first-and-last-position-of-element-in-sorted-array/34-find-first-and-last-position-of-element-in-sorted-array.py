class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums1 = [d for d in nums if d == target]
        return [nums.index(target), nums.index(target) + len(nums1) - 1] if len(nums1) > 0 else [-1, -1]
    # Whole thing is O(n)
    
    