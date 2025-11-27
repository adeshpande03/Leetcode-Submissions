class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Calculate the prefix sum
        ps = [0]
        length = len(nums)
        max_sum = float('-inf')
        for i,num in enumerate(nums):
            ps.append(ps[i] + num)

        for i in range(k):
            current_sum = 0
            # max_sum = max(max_sum, current_sum)
            for n in range(i, length-k+1, k):
                sum_of_next_k_elements = ps[n+k] - ps[n]
                current_sum = max(current_sum + sum_of_next_k_elements, sum_of_next_k_elements)
                max_sum = max(max_sum, current_sum)    
        return max_sum