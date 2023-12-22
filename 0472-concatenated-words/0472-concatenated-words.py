class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str], mi = None) -> List[str]:
        min_len = min(map(len, words))
        word_set = set(words)

        @cache
        def dfs(s) -> bool:  # Return True if s is a concatenated word
            for i in range(min_len, len(s)-min_len+1):
                # Break s into s[:i] and s[i:]
                if s[:i] in word_set and ((t := s[i:]) in word_set or dfs(t)):
                    return True
            return False

        return [s for s in words if dfs(s)]