class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cA = Counter(word1)
        cB = Counter(word2)
        diff1 = cA - cB
        diff2 = cB - cA
        print(diff1, diff2)
        for i in diff2:
            if diff2[i] > 3:
                return False
        for i in diff1:
            if diff1[i] > 3:
                return False
        return True
