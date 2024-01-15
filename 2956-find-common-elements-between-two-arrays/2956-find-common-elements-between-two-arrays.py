class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * 2
        n1, n2 = set(nums1), set(nums2)
        for i in nums1:
            if i in n2:
                res[0] += 1
        
        for i in nums2:
            if i in n1:
                res[1] += 1

        return res