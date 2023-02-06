class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = int(len(nums)/2)
        il = nums[:half]
        ul = nums[half:len(nums)]
        fl = sum(map(list, list((zip(il, ul)))), [])
        return (fl)
        