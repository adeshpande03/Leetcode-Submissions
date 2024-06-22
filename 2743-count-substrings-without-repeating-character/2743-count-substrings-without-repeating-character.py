class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        ans = 0
        for ridx, c in enumerate(s):
            ans += 1
            teststr = c
            lidx = ridx - 1
            while 0 <= lidx and s[lidx] not in teststr:
                teststr = s[lidx]+teststr
                ans += 1
                lidx -= 1
        
        return ans