
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if math.log2(n) % 1 == 0 else False