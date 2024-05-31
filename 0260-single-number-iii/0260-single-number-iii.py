class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
                return Counter(nums).most_common()[-1][0], Counter(nums).most_common()[-2][0], 