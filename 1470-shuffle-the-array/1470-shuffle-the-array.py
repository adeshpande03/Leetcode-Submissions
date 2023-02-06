class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return sum(map(list, list((zip(nums[:len(nums)//2], nums[len(nums)//2:len(nums)])))), [])
    
        