class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        posNeg = 1
        while s[0] == ' ':
            s = s[1:]
            if len(s) == 0:
                return 0
        if s[0] == '-':
            posNeg = -1
            s = s[1:]
        elif s[0] == '+':
            posNeg = 1
            s = s[1:]
        if len(s) == 0:
            return 0
        t = []
        i = 0
        while (s[i].isdigit()):
            t.append(s[i])
            i += 1
            if i == len(s):
                break
        if len(t) == 0:
            return 0
        num = int((''.join(t))) * posNeg
        print(num)
        if num < -(2**31):
            num = -(2**31)
        elif num > 2**31 - 1:
            num = 2**31 - 1
        return num
        