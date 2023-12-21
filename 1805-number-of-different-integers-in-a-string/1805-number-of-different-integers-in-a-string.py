class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l = ''
        for i in word:
            if i.isalpha():
                l += " "
            else:
                l += i
        return (len(set((map(int, l.split())))))