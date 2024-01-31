class Solution:
    def maxDepthAfterSplit(self, seq):
        return [i & 1 ^ (seq[i] == '(') for i, c in enumerate(seq)]