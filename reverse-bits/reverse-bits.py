class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(reversed([n for n in str('{:032b}'.format(n))])), 2)