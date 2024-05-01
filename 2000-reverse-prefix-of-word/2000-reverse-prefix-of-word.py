class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            l = word.index(ch)
            return word[:l + 1][::-1] + word[l+1:]
        return word