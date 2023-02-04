class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num1, num2 = set(nums1), set(nums2)
        return min(num2.intersection(num1)) if num2.intersection(num1) else -1