class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        worklist = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    worklist.append((i, j))
        self.sovle_sigle_case(board, worklist, 0)
    def sovle_sigle_case(self, board, worklist, work_idx):
        if work_idx >= len(worklist):
            return True
        cur = worklist[work_idx]
        spare_cdd = self.get_cdd(board, cur[0], cur[1])
        if len(spare_cdd) == 0:
            return False

        for ele in spare_cdd:
            board[cur[0]][cur[1]] = ele
            res = self.sovle_sigle_case(board, worklist, work_idx + 1)
            if res == True:
                return True
            else:
                board[cur[0]][cur[1]]== "."
        return False


    def check_row(self, board, row):
        cdd = {"1","2","3","4","5","6","7","8","9"}
        for i in range(1, 10):
            if board[row][i] in cdd:
                cdd.remove(board[row][i])
        return cdd

    def chcke_col(self, board, col):
        cdd = {"1","2","3","4","5","6","7","8","9"}
        for i in range(1, 10):
            if board[i][col] in cdd:
                cdd.remove(board[i][col])
        return cdd

    def check_table(self, board, row, col):
        zone_r = int(row / 3)
        zone_c = int(col / 3)
        cdd = {"1","2","3","4","5","6","7","8","9"}
        for r_delta in range(3):
            r_idx = zone_r * 3 + r_delta
            for c_delta in range(3):
                c_idx = zone_c * 3 + c_delta
                if board[zone_r][zone_c] in cdd:
                    cdd.remove(board[zone_r][zone_c])
        return cdd
    def get_cdd(self, board, row, col, cdd):
        col_cdd = self.chcke_col(board, col)
        row_cdd = self.check_row(board, row)
        table_cdd = self.check_table(board,row, col)
        fin_cdd = row_cdd.intersection(table_cdd).intersection(col_cdd)
        return fin_cdd