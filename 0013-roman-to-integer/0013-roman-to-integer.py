class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        count = 0
        while ('IV' in s or 'IX' in s or 'XL' in s or 'XC' in s or 'CD' in s or 'CM' in s) and len(s) > 0: 
            if 'IV' in s:
                count += 4
                s = s.replace('IV', '')
                print(s)
            if 'IX' in s:
                count += 9
                s = s.replace('IX', '')
                print(s)
            if 'XL' in s:
                count += 40
                s = s.replace('XL', '')
            if 'XC' in s:
                count += 90
                s = s.replace('XC', '')
            if 'CD' in s:
                count += 400
                s = s.replace('CD', '')
            if 'CM' in s:
                count += 900
                s = s.replace('CM', '')
            
        for i in s:
            if i in romans:
                count += romans[i]
        return (count)