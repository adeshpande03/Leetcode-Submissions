class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        def startsVowel(word):
            if word[0] in vowels and word[-1] in vowels:
                return 1
            return 0
        words = list(map(startsVowel, words))
        for i in range(1, len(words)):
            words[i] += words[i - 1]
        print(words)
        ans = []
        for i in queries:
            if i[0] == 0:
                ans.append(words[i[-1]])
            else:
                ans.append(words[i[-1]] - words[i[0] - 1])
        return ans