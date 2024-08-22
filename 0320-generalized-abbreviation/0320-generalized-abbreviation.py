class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.perms = []
        self.generateGeneralizedAbbreviationHelper(word, 0, "", 0)
        return self.perms

    def generateGeneralizedAbbreviationHelper(self, word, index, perm, count):
        if index == len(word):
            if count:
                perm += str(count)

            self.perms.append(perm)
            return 

        self.generateGeneralizedAbbreviationHelper(word, index+1, perm, count+1)  # Branch 1: increase the count
        if count:
            perm += str(count)  # O(n) to copy the current permutation

        self.generateGeneralizedAbbreviationHelper(word, index+1, perm + word[index], 0)  # Branch 2: append the count and append the current char