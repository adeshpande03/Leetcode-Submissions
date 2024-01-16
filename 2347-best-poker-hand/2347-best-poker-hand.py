class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        c = Counter(ranks)
        if c.most_common()[0][1] >= 3:
            return "Three of a Kind"
        if c.most_common()[0][1] == 2:
            return "Pair"
        return "High Card"