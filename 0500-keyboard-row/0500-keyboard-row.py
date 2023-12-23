class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = []
        for word in words:
            if (set(word.lower()).intersection(set('qwertyuiop'))) == (set(word.lower())):
                a.append(word)
            if (set(word.lower()).intersection(set('asdfghjkl'))) == (set(word.lower())):
                a.append(word)
            if (set(word.lower()).intersection(set('zxcvbnm'))) == (set(word.lower())):
                a.append(word)
        return a