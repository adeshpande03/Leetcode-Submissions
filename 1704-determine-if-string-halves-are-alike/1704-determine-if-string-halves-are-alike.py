class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        return sum([i in vowels for i in s[:len(s)//2]]) == sum([i in vowels for i in s[len(s)//2:]])
            
            