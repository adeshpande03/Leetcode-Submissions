class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        
        dominoes = [tuple(sorted(d)) for d in dominoes]
        c = Counter(dominoes)
        print(c)
        for i in c:
            if c[i] >= 2:
                n = c[i]
                ans += (n * (n - 1))//2
        return ans