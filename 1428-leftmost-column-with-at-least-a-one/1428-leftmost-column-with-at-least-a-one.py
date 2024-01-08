# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
            rows, cols = binaryMatrix.dimensions()
            left, right = 0, cols -1
            while left <= right:
                mid = (left + right) // 2
                seen = any([binaryMatrix.get(r, mid) for r in range(rows)])
                if left == right:
                    return -1 if not seen else left        
                if seen:
                    right = mid   
                else:
                    left = mid + 1