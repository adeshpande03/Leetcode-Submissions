class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        if len(s) < 2:
            return []
        for i in range(len(s) - 1):
            c = s[i: i + 2]
            if '++' == c:
                ans.append(s[:i] + '--' + s[i + 2:])
        return ans
                