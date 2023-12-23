class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            s = 0
            while num > 0:
                r = num % 10
                s += r**2
                num = num // 10
            return s
        seen = set()
        while True:
            n = sqr(n)
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True
        return False