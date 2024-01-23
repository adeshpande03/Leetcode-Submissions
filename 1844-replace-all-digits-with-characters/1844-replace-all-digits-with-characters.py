class Solution:
    def replaceDigits(self, s: str) -> str:
        l = list(s)
        for idx in range(len(l)):
            if l[idx].isdigit():
                l[idx] = chr(int(l[idx]) + ord(l[idx - 1]))
        return ''.join(l)