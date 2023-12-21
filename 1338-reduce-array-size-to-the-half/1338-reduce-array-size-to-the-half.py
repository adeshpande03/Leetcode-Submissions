class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)//2
        c = Counter(arr)
        ans = 0
        for d in (c.most_common()):
            l-= d[1]
            ans += 1
            if l <= 0:
                break
        print(c)
        return ans
        