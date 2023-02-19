class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n == 1:
            return False
        sq = int(sqrt(n))
        s = 1
        for i in range(2, sq+1):
            if n % i==0:
                t = n // i
                s += t + i
        return s == n