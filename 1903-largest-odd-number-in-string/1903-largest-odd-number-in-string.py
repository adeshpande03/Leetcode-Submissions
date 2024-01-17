class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = set('13579')
        for i,j  in enumerate(num[::-1]):
            if j in odd:
                return num[:len(num) - i]
        return ''
                