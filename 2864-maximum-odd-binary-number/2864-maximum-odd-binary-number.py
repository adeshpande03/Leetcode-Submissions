class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count('1') - 1
        l = len(s)
        return ('1' + (l - c - 1)*'0' + c * '1')[::-1]