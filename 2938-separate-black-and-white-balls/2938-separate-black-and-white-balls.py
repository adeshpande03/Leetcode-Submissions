class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # Take the zero count
        zero_count = 0
        moves = 0

        # Traverse from right to left
        # Check for zeroes on the right
        # The number of zeroes on right is the number of moves required
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                zero_count += 1
            else:
                moves += zero_count

        return moves
        