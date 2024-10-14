class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapify(nums)
        ans = 0
        for _ in range(k):
            temp = -heappop(nums)
            ans += temp
            heappush(nums, -1 * ceil(temp/3))
        return ans
            