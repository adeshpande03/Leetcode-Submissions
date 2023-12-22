class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        ans = (bin(k + 1)[2:])
        s = ''
        for i in range(len(ans)):
            if ans[i] == "1":
                s += '7'
            else:
                s += "4"
        return s[1:]