class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse = True)
        s = 0
        for i in range(k):
            s += max(h[i] - i, 0)
        return s
