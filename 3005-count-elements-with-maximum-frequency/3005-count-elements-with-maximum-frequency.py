class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = c.most_common()
        d = 0
        n = m[0][1]
        for i in c:
            if c[i] == n:
                d += n
            
        return d
            