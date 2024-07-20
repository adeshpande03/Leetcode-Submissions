class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []
        colIndex = 0
        for row in rowSum:
            matrixRow = [0] * colIndex
            while colIndex < len(colSum):
                col = colSum[colIndex]
                if row < col:
                    colSum[colIndex] -= row
                    matrixRow.append(row)
                    break
                else:
                    colIndex += 1
                    matrixRow.append(col)
                    row -= col
                    if row == 0:
                        break
            matrixRow.extend([0] * (len(colSum) - len(matrixRow)))
            matrix.append(matrixRow)
        return matrix