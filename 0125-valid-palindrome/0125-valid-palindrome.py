class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = [d.lower() for d in s if d.isalpha() or d.isdigit()]
        return stripped == list(reversed(stripped))