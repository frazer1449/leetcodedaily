# Prefix Sum
# Range Sum Query 2D Immutable

# You are given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = []
        for c in len(matrix[0]):
            row.append(matrix[r][c])
        self.matrix.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        m, n = len(matrix), len(matrix[0])
        # 0 is not a mutable object
        # [0, 0, ... , 0] is a mutable object
        prefix = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                prefix[r][c] = matrix[r][c]
                if r > 0:
                    prefix[r][c] += prefix[r-1][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c-1]
                if r > 0 and c > 0:
                    prefix[r][c] -= prefix[r-1][c-1]
        
        ans = prefix[row2][col2]
        if row1 > 0:
            ans -= prefix[row1-1][col2]
        if col1 > 0:
            ans -= prefix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            ans += prefix[row1-1][col1-1]
        
        return ans
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)