class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        for k in range(len(nums) - 1, 0, -1):
            l = nums[0:k]
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                        diff = l[i] - l[j]
                        m = max(m, diff * nums[k])
        
        return m


