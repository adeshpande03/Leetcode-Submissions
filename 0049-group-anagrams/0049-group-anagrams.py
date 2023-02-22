from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            if str(sorted(i)) in d:
                d[str(sorted(i))].append(i)
            else:
                d[str(sorted(i))] = [i]
        return (list(d.values()))
            