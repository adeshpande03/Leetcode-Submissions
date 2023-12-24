class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i == '../':
                c = max(0, c - 1)
            elif i == './':
                continue
            else:
                c += 1
        return c
            