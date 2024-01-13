class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        trimmed = defaultdict(list)
        trimDigits = set([trimDigit for _, trimDigit in queries])
        for trimDigit in trimDigits:
            for idx, num in enumerate(nums):
                trimmed[trimDigit].append((num[-trimDigit :], idx))
            trimmed[trimDigit].sort()  
        return [trimmed[trimDigit][k - 1][1] for k, trimDigit in queries]