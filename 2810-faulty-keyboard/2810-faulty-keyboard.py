class Solution:
    def finalString(self, s: str) -> str:
        prev = ''
        for i in s:
            if i != 'i':
                prev += i
            else:
                prev = prev[::-1]
        return prev
            