class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n, cost = len(nums), lambda x : sum([abs(x-a) for a in nums])
        nums.sort()
        med = nums[n//2]
        left, right = med-1, med+1
        while str(left) != str(left)[::-1]:
            left -= 1
        while str(right) != str(right)[::-1]:
            right += 1
        
        res = [left, right]
        if str(med) == str(med)[::-1]:
            res.append(med)
        best = min(res, key = cost)
        return cost(best)
