class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common = list(set(text1) & set(text2))
        if len(common) == 0:
            return 0
        text1 = [c for c in text1 if c in common]
        text2 = [c for c in text2 if c in common]
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        dynamic = [0 for i in text1]
        for c in text2:
            count = 0
            for i in range(len(text1)):
                if count < dynamic[i]:
                    count = dynamic[i]
                elif c == text1[i]:
                    dynamic[i] = count + 1
        return max(dynamic)
