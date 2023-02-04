class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        
        for _ in range(4):
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # Reverse each row in the matrix
            for row in matrix:
                row.reverse()
            if matrix == target:
                return True
        return False
                
        