class Solution:
    def alternateDigitSum(self, n: int) -> int:
        c = 0
        s = str(n)
        for i in range(len(s)):
            if i % 2 == 0:
                c += int(s[i])
            else:
                c -= int(s[i])
        return c
            