class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def s(value):
            if value == 2 or value == 3:
                return 1
            if value == 4 :
                return 2
            if value > 4:
                return 1 + s(value - 3)
        
        c = Counter(nums)
        
        return -1 if any([val == 1 for val in c.values()]) else sum([s(val) for val in c.values()])