class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = len(nums)
        c = Counter(nums)
        return c[target] > l/2