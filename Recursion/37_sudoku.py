class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        cols = len(board[0])
        rows = len(board)
        candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # 9 zones can be distinguished by mod 3
        # 3 x 3
        for row in rows:
            for col in cols:
                if row % 3 == col % 3:
                    if board[row][col] in candidates:
                        candidates.remove(board[row][col])





