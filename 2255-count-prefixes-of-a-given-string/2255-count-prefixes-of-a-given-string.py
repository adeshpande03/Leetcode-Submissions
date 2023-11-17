class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in range(len(s) + 1):
            res += words.count(s[:i])
        return res
            