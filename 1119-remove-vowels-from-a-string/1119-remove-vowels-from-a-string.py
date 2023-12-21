class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([d for d in s if d not in 'aeiou'])