class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        il = s.split()
        return len(il[-1])