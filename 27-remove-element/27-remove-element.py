class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [d for d in nums if d != val]
        return len(nums)

        
        