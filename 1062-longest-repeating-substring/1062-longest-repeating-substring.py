class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        ans =0

        def kmp(start):
            p = [0]* len(s)
            res =0
            j = start
            for i in range(start+1, len(s)):
                while j > start and s[j] != s[i]:
                    j = p[j-1] + start
                
                if s[i] ==s[j]:
                    j +=1
                    p[i] = j - start
                res = max(res, j-start)
            return res
        for i in range(len(s)):
            ans = max(ans, kmp(i))
        return ans
