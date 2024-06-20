from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions
        position.sort()
        
        # Helper function to check if we can place m balls with at least `min_force` distance apart
        def canPlaceBalls(min_force):
            count = 1
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        # Binary search for the maximum minimum distance
        left, right = 1, position[-1] - position[0]
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right

# Example Usage
solution = Solution()
print(solution.maxDistance([1, 2, 3, 4, 7], 3))  # Output: 3
print(solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))  # Output: 999999999