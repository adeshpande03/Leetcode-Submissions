class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r=[]
        for i in operations:
            if i == 'C':
                r=r[:-1]
            elif i == 'D':
                r += [int(r[-1] * 2)]
            elif i == '+':
                r += [int(r[-1] + r[-2])]
            else:
                r.append(int(i))
        return sum(r)