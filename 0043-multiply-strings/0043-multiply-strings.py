class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        f = int(num1)
        g = int(num2)
        totalf = 0
        totalg = 0
        ilf = []
        ilg = []
        for i in range(len(num1)):
            totalf += 10**i*int(num1[len(num1) - 1 - i])
        for i in range(len(num2)):
            totalg += 10**i*int(num2[len(num2) - 1 - i])
        return(str(totalf * totalg))
        