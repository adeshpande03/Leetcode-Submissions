class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def substract(value):
            if value == 2 or value == 3:
                return 1
            if value == 4 :
                return 2
            if value > 4:
                return 1 + substract(value - 3)
        
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        return -1 if any([val == 1 for val in hashmap.values()]) else sum([substract(val) for val in hashmap.values()])