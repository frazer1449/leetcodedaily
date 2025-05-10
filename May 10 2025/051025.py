# Topic: Math & Geometry, Level: Medium

# Rotate

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # rotation by 90 = transpose + reflect across y-axis

        # 1 2 3.  1 4 7.  7 4 1  
        # 4 5 6.  2 5 8.  8 5 2
        # 7 8 9.  3 6 9.  9 6 3
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
