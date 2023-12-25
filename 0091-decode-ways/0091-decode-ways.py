class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def m(i, s):
            if i == len(s):

                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:

                return 1
            a = m(i + 1, s)
            if int(s[i:i + 2]) <= 26:
                a += m(i + 2, s)
            return a
        return m(0, s)