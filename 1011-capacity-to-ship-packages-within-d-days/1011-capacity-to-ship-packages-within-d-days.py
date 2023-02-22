class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = max(weights)
        totalWeight = sum(weights)
        l, r = maxWeight, totalWeight
        
        while l < r:
            mid = (l + r) // 2
            daysNeeded, currWeight = 1, 0
            
            for weight in weights:
                if currWeight + weight > mid:
                    currWeight = 0
                    daysNeeded += 1
                currWeight += weight
                
            if daysNeeded <= days:
                r = mid
            else:
                l = mid + 1
        return l
        