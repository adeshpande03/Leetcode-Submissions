class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        k = n // 2
        for i in range(k):
            ans.append(-i - 1)
            ans.append(i + 1)
        if n % 2 == 1:
            ans.append(0)
        return ans
