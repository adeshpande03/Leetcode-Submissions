class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        il = [nums[k:k + 3] for k in range(0, len(nums), 3)]
        for test in il:
            if abs(test[-1] - test[0]) > k or abs(test[1] - test[0]) > k:
                return []
        return il