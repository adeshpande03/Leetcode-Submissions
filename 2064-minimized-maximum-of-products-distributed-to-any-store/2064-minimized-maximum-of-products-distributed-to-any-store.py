class Solution:
    def minimizedMaximum(self, n: int, q: List[int]) -> int:
        return bisect_left(range(1, max(q)), 0, key = lambda p :n-sum(ceil(qq/p) for qq in q))+1