class Solution:
    def recursion(self, n):
        if n <= 26:
            return chr(n)
        a = ''
        a = self.recursion(n // 26) + self.recursion(n % 26)
        return a
    def convertToTitle(self, n):
        il = []
        b = self.recursion(n)
        for i in b:
            il.append(ord(i))
        while 0 in il:
            if il[0] == 0:
                il.pop(0)
            for i in range(len(il)):
                if il[i] == 0:
                    il[i] += 26
                    il[i - 1] -= 1
        for i in range(len(il)):
            il[i] = chr(il[i] + 64)
        return ''.join(il)

        

