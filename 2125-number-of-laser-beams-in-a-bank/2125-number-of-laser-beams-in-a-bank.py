class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [l for l in bank if set(l) != {'0'}]
        s = 0
        for n in range(1, len(bank)):
            s += bank[n - 1].count('1') * bank[n].count('1')
        return s
            