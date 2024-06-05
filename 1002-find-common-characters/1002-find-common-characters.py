class Solution(object):
    def commonChars(self, words):
        ans = []
        cnt = Counter(words[0])
        for word in words:
            cnt&=Counter(word)
        
        for element in cnt:
            for i in range(cnt[element]):
                ans.append(element)
        return ans