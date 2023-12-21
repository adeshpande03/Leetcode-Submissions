class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = moves.count('_')
        l = moves.count('L')
        r = len(moves) - c - l
        return (abs(l - r) + c)