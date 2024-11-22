class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        #save grid value and its position
        memo = [(grid[r][c], r, c) for c in range(n) for r in range(m)]

        #sort based on the value
        memo.sort() 

        #list for keep the maximum value for each row, column
        rowMax = [0] * m
        colMax = [0] * n

        #for each element in memo
        for v, r, c in memo:
            #get maximum of given row, column and +1 to keep order
            grid[r][c] = max(rowMax[r], colMax[c]) + 1

            #update maximum value of each row, column
            rowMax[r] = colMax[c] = grid[r][c]
        return grid