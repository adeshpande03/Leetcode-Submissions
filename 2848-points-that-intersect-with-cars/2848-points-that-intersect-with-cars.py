class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for n in nums:
            s.update(set(range(n[0], n[1] + 1)))
        return len(s)