class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        else:
            code = 2*code
        start = 0
        if k < 0:
            start = len(code)//2
        ans = [0] * (len(code)//2)
        for i in range(start, start + len(code)//2):
            if k > 0:
                ans[i] += sum(code[i+1: i + k + 1])
            else:
                ans[i - start] += sum(code[i + k : i])
        return ans