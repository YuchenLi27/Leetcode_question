class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        work_list = []
        for row_i in range(9):
            for col_i in range(9):
                if board[row_i][col_i] == ".":
                    work_list.append((row_i, col_i))
        self.solve_single_point(board, work_list, 0)
        return board

    def solve_single_point(self, board, work_list, work_i):
        if work_i >= len(work_list):
            return True
        cur_point = work_list[work_i]
        point_candidate = self.get_candiadate_number(cur_point[0], cur_point[1], board)
        if len(point_candidate) == 0:
            return False

        for num in point_candidate:
            board[cur_point[0]][cur_point[1]] = num
            result = self.solve_single_point(board, work_list, work_i + 1)
            if result == True:
                return True
            else:
                board[cur_point[0]][cur_point[1]] = "."
        return False

    def check_row_candidate(self, row_i, board):
        full_set = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for i in range(9):
            if board[row_i][i] != ".":
                full_set.remove(board[row_i][i])
        return full_set

    def check_col_candidate(self, col_i, board):
        full_set = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for i in range(9):
            if board[i][col_i] != ".":
                full_set.remove(board[i][col_i])
        return full_set

    def check_table_candidate(self, row_i, col_i, board):
        # check 9 x 9
        full_set = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        row_base = int(row_i / 3)
        col_base = int(col_i / 3)
        for row_delta in range(3):
            row_index = row_base * 3 + row_delta
            for col_delta in range(3):
                col_index = col_base * 3 + col_delta
                if board[row_index][col_index] != ".":
                    full_set.remove(board[row_index][col_index])
        return full_set

    def get_candiadate_number(self, row_i, col_i, board):
        row_candidate = self.check_row_candidate(row_i, col_i, board)
        col_candidate = self.check_col_candidate(row_i, col_i, board)
        table_candidate = self.check_table_candidate(row_i, col_i, board)
        final_candidate = row_candidate.intersection(col_candidate).intersection(table_candidate)
        return final_candidate


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    res = Solution().solveSudoku(board)
    print(res)