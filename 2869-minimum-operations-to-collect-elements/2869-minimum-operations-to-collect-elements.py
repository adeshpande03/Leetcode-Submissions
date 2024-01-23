class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = set(range(1, 1 + k))
        print(r)
        nums[:] = nums[::-1]
        for i in range(1, len(nums) + 1):
            print(set(nums[:i]))
            if r.issubset(set(nums[:i])):
                return i
        return 0