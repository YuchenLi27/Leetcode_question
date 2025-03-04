"""
zigzag string, the rowNums + 1 will be added to the last row array

"""
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = [""] * numRows

        idx = 0
        d = 1
        for ele in s:
            rows[idx].append(ele)

            if idx == 0: # if this is the first ele, move down, until it reaches to the last row
                d = 1
            elif idx == numRows - 1: # last row
                d = -1
            idx += d # move ele to the limit (the numRow)

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)