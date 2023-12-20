class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        c = sum(list(sorted(prices))[:2])
        return money - c if money - c >= 0 else money