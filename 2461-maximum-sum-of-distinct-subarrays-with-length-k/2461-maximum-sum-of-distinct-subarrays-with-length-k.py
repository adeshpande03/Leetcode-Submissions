class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, ans, pref_sum  = 0, 0, 0
        cnt_nums = defaultdict(int)
        for right, num in enumerate(nums):
            pref_sum += num
            cnt_nums[num] += 1 
            if right >= k:
                cnt_nums[nums[left]] -= 1
                if cnt_nums[nums[left]] == 0:
                    del cnt_nums[nums[left]]
                pref_sum -= nums[left]
                left += 1
            if len(cnt_nums) == k:
                ans = max(pref_sum, ans)
        return ans