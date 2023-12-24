class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s1 = dict(Counter(s1))
        s2 = dict(Counter(s2))
        res = []
        for i in s1:
            if s1[i] == 1 and i not in s2:
                res.append(i)
        for i in s2:
            if s2[i] == 1 and i not in s1:
                res.append(i)
        return res
                