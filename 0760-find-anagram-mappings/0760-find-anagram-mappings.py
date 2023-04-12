class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        for i in A:
            result.append(B.index(i))
        return result