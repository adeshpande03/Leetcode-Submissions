class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row: List[str]):
            d = {}
            placeholder = 0
            for i in row:
                if i not in d and i != '.':
                    d[i] = row.count(i)
            for i in d:
                if d[i] > 1:
                    placeholder += 1
            if placeholder > 0:
                return False
            return True
        def checkAllRows(board: List[List[str]]):
            for i in board:
                if checkRow(i) == False:
                    return False
            return True
        def checkColumnJ(board: List[List[str]], j):
            i = 0
            d = {}
            il = []
            while i < 9:
                il.append(board[i][j])
                i += 1
            for i in il:
                if i != '.' and i not in d:
                    d[i] = il.count(i)
            for i in d:
                if d[i] > 1:
                    return False
            return True
        def check3x3(board: List[List[str]],a, b):
            il = []
            d = {}
            for i in range(3*a, 3*(a + 1)):
                for j in range(3*b, 3*(b + 1)):
                    if board[i][j] != '.':
                        il.append(board[i][j])
            for i in il:
                if i != '.' and i not in d:
                    d[i] = il.count(i)
            for i in d:
                if d[i] > 1:
                    return False
            return True
        def checkall3(board: List[List[str]]): 
             for i in range(3):
                for j in range(3):
                    if check3x3(board, i, j) == False:
                        return False
            
             return True
        def checkallColumns(board: List[List[str]]):
            for i in range(9):
                if checkColumnJ(board, i) == False:
                    return False
            return True
        print(checkall3(board), checkallColumns(board), checkAllRows(board))
        for i in range(3):
            for j in range(3):
                print(check3x3(board,i,j))
        if checkall3(board) and checkAllRows(board) and checkallColumns(board):
            return True
        return False