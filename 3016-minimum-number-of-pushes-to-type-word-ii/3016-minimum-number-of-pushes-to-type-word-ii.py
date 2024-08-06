class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word).most_common() 
        c.insert(0,0)
        n = 1
        t = 0
        for i in range(1, len(c)):
            t += n * c[i][1]
            if (i % 8) == 0:
                n += 1
        return t