class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums[:] = sorted([int(d) for d in nums])
        return str(nums[-k])