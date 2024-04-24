class Solution:
    def tribonacci(self, n: int) -> int:

        l = [0, 1, 1]
        if n <= 2:
            return l[n]
        for _ in range(n - 2):
            l.append(sum(l[-3:]))
            l = l[1:]
        return l[-1]
