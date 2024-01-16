class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(str1_length, str2_length)]