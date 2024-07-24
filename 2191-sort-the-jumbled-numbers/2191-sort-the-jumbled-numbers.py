class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key= lambda n: reduce(lambda m, i: m*10+mapping[int(i)], str(n), 0))