class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        cost.sort()
        c = 0
        while len(cost) > 2:
            c += sum(cost[-2:])
            cost = cost[0:-3]
        return c + sum(cost)