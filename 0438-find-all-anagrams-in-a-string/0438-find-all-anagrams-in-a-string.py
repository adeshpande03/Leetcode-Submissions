class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        ans = []
        for _ in range(len(s) - len(p) + 1):
            if sorted(s[_:len(p) + _]) == p:
                ans.append(_)
        return ans
        