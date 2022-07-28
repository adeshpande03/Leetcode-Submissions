class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = []
        tl = []
        sl[:0] = s
        tl[:0] = t
        return True if sorted(sl) == sorted(tl) else False