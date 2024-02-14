class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a, b, ans = [], [], []
        for num in nums:
            if num > 0:
                a.append(num)
            else:
                b.append(num)
        
        for i in range(len(nums)):
            if not i % 2:
                ans.append(a[i//2])
            else:
                ans.append(b[i//2])
        return ans
