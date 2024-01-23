class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        grp = groupby(nums, key = lambda x: x.bit_count())
        
        return list(chain.from_iterable([sorted(g) for _, g in grp])) == sorted(nums)