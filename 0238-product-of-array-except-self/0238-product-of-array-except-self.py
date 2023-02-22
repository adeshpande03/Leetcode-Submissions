class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] *= nums[i] * prefix[i - 1]
        r = list(reversed(nums))
        for i in range(len(r)):
            postfix[i] *= r[i] * postfix[i - 1]
        postfix.reverse()
        print(postfix)
        print(prefix)
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]
        return nums
        