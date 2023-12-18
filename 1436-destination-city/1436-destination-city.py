class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {i[0] : i[1] for i in paths}
        print(d)
        for c in d:
            if d.get(d.get(c, 0), 0) == 0:
                return d[c]
        