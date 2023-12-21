class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = moves.count('_')
        l = moves.count('L')
        return (abs(2*l + c - len(moves)) + c)