class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money - sum(list(sorted(prices))[:2]) if money - sum(list(sorted(prices))[:2]) >= 0 else money