class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            i = str(num)
            if l:=len(i) % 2 == 1:
                continue
            else:
                l = len(i)
                n = l//2
                i = [int(d) for d in i]
                if sum(i[:n]) == sum(i[n:]):
                    ans += 1
        return ans