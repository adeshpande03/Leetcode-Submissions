class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}
        def backtrack(p_index, s_index):
            if p_index == len(pattern):
                return s_index == len(s)
            p = pattern[p_index]
            if p in pattern_to_word:
                word = pattern_to_word[p]
                if s[s_index: s_index+len(word)] != word:
                    return False
                return backtrack(p_index+1, s_index + len(word))
            else:
                for k in range(1, len(s)-s_index+1):
                    word = s[s_index:s_index+k]
                    if word in word_to_pattern:
                        continue
                    pattern_to_word[p] = word
                    word_to_pattern[word] = p
                    if backtrack(p_index+1, s_index+len(word)):
                        return True
                    del pattern_to_word[p]
                    del word_to_pattern[word]  
        return backtrack(0,0)