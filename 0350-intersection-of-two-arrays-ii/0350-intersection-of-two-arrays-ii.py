class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        return [d for d in a if d in b]