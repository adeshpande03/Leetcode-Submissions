class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l = []
        r = ''
        def c(s):
            if not s:
                s = '0'
            return int(s, 2) % 5 == 0
        for i in nums:
            r += str(i)
            l.append(c(r))
        return l


