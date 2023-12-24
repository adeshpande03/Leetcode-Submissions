class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d = list(itertools.permutations(digits, 3))
        res = set()
        for i in d:
            if not i[-1] % 2 and i[0] != 0:
                res.add(int(''.join([str(g) for g in i])))
        return sorted(list(res))