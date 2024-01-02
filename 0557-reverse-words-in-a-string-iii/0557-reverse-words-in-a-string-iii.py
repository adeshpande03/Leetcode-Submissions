class Solution:
    def reverseWords(self, s: str) -> str:
        f = s.split()
        return ' '.join([s[::-1] for s in f])