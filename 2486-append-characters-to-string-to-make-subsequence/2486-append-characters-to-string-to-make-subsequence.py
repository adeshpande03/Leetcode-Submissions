class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        start = 0
        for c in s:
            if start >= len(t):
                return 0
            if c == t[start]:
                start += 1
        # t[start:] is the non inside s string
        return len(t[start:])