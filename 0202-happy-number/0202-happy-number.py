class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            sum = 0
            while num > 0:
                r = num % 10
                sum += r**2
                num = num // 10
            return sum
        seen = set()
        while True:
            n = sqr(n)
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True
        return False