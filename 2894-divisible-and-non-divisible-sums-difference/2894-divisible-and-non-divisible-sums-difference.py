class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([d if (d % m != 0) else -d for d in range(1, n + 1)])