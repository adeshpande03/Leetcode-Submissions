class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return True
        return False