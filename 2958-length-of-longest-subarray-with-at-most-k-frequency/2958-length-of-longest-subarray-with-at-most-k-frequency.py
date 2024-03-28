class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, d = len(nums), defaultdict(int)
        i, j, ans = 0, 0, 0
        while j < n:
            if d[nums[j]] == k:
                d[nums[i]] -= 1
                i += 1
            elif d[nums[j]] < k:
                d[nums[j]] += 1
                j += 1
            ans = max(ans, j - i)
        return ans
