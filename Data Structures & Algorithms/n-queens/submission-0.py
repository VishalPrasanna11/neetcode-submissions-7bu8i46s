class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []
        board = [['.']*n for _ in range(n)]

        def convert_board(board):
            return ["".join(row) for row in board]

        def isValid(row, col, board):

            #check wih row

            for x in range(row):
                if board[x][col]== "Q":
                    return False
            #Top Left Diagonal

            for r, c in zip(range(row -1, -1, -1 ) , range(col-1, -1, -1)):

                if board[r][c] == "Q":
                    return False
            
            #Top Right Diagonla

            for r, c in zip(range(row - 1, -1, -1) , range(col+1,n)):
                if board[r][c] == "Q":
                    return False
            

            return True

        def solve(board, row):

            if row == n:
                result.append(convert_board(board))
                return

            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = "Q"
                    solve(board,row+1)
                    board[row][col] = "."

        solve(board, 0)
        return result