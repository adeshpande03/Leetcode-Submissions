class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([len(d) for d in words if all([d.count(i) <= chars.count(i) for i in d])])