class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        text = text.split()
        c = 0
        b = set(b)
        for word in text:
            if len(set(word).intersection(b)) == 0:
                c += 1
        return c