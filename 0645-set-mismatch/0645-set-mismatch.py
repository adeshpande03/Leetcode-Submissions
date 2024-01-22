class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)- (c:=sum(set(nums))), (d:=len(nums))*(d+1)//2-c]
        