class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        res = [i.start() for i in re.finditer(a, s)]
        bs = [i.start() for i in re.finditer(b, s)]
        ans = []
        for i in res:
            for t in (bs):
                if abs(i - t) <= k:
                    ans.append(i)
                    break
        return (ans)