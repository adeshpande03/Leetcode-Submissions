class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        charToID = dict()
        maxDist = -1
        
        for i, ch in enumerate(s):
            if ch not in charToID:
                charToID[ch] = i
            else:
                maxDist = max(maxDist, i - charToID[ch] -1)
        
        return maxDist