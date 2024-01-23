class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = [i % 26 for i in list(accumulate(shifts[::-1]))][::-1]
        s = list(s)
        for i in range(len(s)):
            d = (ord(s[i]) + shifts[i])
            if d > 122:
                d -= 26
            s[i] = chr(d)
        return ''.join(s)