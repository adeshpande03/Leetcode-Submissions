class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [*zip(*sorted(zip(map(neg, heights), names)))][1]