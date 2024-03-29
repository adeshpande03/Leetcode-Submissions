class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(map(list, zip(*matrix)))
        for i in range(len(matrix)):
            matrix[i].reverse()