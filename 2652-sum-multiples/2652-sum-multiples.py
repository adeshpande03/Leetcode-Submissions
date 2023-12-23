class Solution:
    def sumOfMultiples(self, n: int) -> int:
        c = 0
        for i in range(1, n + 1):
            if not (i%3 and i%5 and i%7):
                c += i
        return c