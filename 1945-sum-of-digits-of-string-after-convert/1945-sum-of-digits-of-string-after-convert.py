class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        def c(s):
            t = ''
            for i in s:
                t += str(ord(i) - 96)
            return t
        s = c(s)
        def r(s):
            g = 0
            for i in s:
                g += int(i)
            return str(g)
        for i in range(k):
            s = r(s)
        return int(s)