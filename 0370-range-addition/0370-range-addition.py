class Solution:
    def getModifiedArray(self, n: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * n
        c = Counter(map(tuple, updates))
        print(c)
        for num in range(len(ans)):
            for u in c:
                if u[0] <= num <= u[1]:
                    ans[num] += u[2] * c[u]
        return ans