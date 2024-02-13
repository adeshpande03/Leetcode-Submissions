class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def i(s):
            return s == s[::-1]
        for w in words:
            if i(w):
                return w
        return ''