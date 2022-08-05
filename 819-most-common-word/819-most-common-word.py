class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        newS1 = ''
        for i in p:
            if i.isalpha() or i == ' ':
                newS1+=i.lower()
            elif i == ',':
                newS1 += (' ')
        print(newS1)
        newS1 = newS1.split()
        print(newS1)
        newS = sorted(newS1, key = newS1.count, reverse = True)
        # newS1.split()
        # newS = sorted(newS1, key = newS1.count, reverse = True)
        print(newS)
        for i in newS:
            if i not in banned:
                return i