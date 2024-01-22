class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def search(i, j, direc):
            ni, nj = i + direc[0], j + direc[1]
            if not (0 <= ni < len(board) and 0 <= nj < len(board[0])):
                return 0
            if board[ni][nj] == "p":
                return 1
            if board[ni][nj] == "B":
                return 0

            return search(ni, nj, direc)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    return (
                        search(i, j, (0, 1))
                        + search(i, j, (1, 0))
                        + search(i, j, (-1, 0))
                        + search(i, j, (0, -1))
                    )
