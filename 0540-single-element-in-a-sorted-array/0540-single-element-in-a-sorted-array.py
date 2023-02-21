class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start , end = 0 , len(nums) -1
        while start < end :
            mid = (start + end) // 2
            if(nums[mid]==nums[mid+1]):
                mid = mid-1
            
            if((mid-start+1)%2!=0):
                end = mid
            
            else:
                start = mid+1
        return nums[start]