class Solution:
    def convertToBase7(self, n: int) -> str:
        neg = False
        if n < 0:
            neg = True
            n = n * -1
        if n == 0:
            return '0'
        digits = []
        while n:
            digits.append(int(n % 7))
            n //= 7
        return ''.join([str(d) for d in digits[::-1]]) if not neg else '-'+''.join([str(d) for d in digits[::-1]])
            
            