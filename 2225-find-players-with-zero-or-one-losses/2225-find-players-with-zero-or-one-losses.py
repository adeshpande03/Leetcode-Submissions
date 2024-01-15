class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        z = list(zip(*matches))
        s1 = set(z[0])
        s2 = (z[1])
        c = Counter(s2)
        print(s2)
        i2 = []
        for i in c:
            if c[i] == 1:
                i2.append(i)
        i2.sort()
        return [sorted(list(s1 - set(s2))), i2]