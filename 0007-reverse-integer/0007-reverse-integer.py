class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        new = 0
        if x < 0:
            x *= -1
            positive = False
        xstr = str(x)
        for i in range(len(xstr)):
            new += int(xstr[-(i+1)])*10**(len(xstr) - i - 1)
        if positive == False:
            new *= -1
        if new > 2**31 -1 or new < -(2**31):
            return 0
        return new
        