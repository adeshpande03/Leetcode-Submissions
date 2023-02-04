class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        for i, j in enumerate(s):
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
        return sum([distance[(ord(i) - 97)] == d[i][1] - d[i][0] - 1 for i in d]) == len(s) / 2
