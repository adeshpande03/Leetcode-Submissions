class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = dict(Counter(nums))
        s = 0
        for i in c:
            if c[i] % 2 == 1:
                s += (c[i] - 1) // 2
                c[i] = 1
            else:
                s += c[i] // 2
                c[i] = 0
        return s, sum(c.values())
                
                