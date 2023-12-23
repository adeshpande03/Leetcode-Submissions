class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = set(' ')
        d = ''
        for m in key:
            if m in s:
                continue
            s.add(m)
            d += m
        a = 'abcdefghijklmnopqrstuvwxyz'
        s = ''
        for m in message:
            s += a[d.index(m)] if m != ' ' else ' '
        return s