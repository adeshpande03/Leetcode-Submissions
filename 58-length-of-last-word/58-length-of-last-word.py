class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        il = s.strip().split()
        return len(il[-1])