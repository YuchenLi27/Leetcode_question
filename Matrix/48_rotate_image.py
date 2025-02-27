"""
this question aims to understand the rotation of matrix in different degree,
like 90, 180, 270 degrees
this question hope the matrix can rotate in 90 degree clock-wise, let the (l, r) exchange.
and then reverse

"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            