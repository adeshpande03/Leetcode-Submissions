class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [5, 3, 2]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1
        
            
