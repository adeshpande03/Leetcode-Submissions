class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        l = c.values()
        return len(set(l)) == len(l)