class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=0
        counter=Counter(nums)
        for num,freq in counter.items():
            if num+1 in counter:
                count=max(count,freq+counter[num+1])
        return count