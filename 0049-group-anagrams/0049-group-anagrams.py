class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            d[str(sorted(i))].append(i)
        return (list(d.values()))
            