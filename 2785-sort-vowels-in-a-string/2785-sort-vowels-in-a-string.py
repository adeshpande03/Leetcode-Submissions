class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIUO'
        s = list(s)
        vowList = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowList.append(s[i])
                s[i] = 0
        vowList.sort()
        ptr = 0
        res = ''
        for i in range(len(s)):
            if s[i] == 0:
                res += vowList[ptr]
                ptr += 1
            else:
                res += s[i]
        return res
        for i in range(len(s)):
            if s[i] == 0:
                s[i] = vowList[ptr]
                ptr += 1
        return ''.join(s)