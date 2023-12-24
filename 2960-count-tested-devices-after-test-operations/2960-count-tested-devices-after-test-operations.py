class Solution:
    def countTestedDevices(self, A: List[int]) -> int:
        k = 0
        for a in A:
            k += a > k
        return k 