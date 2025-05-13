# Topic: Math & Geometry, Level: Medium

# Spiral Matrix

# Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()
        directions = [[0, 1],[1, 0],[0, -1], [-1, 0]]
        d = 0
        n = 0

        def dfs(i: int, j: int):
            nonlocal d, n, res, visited
            res.append(matrix[i][j])
            visited.add((i, j))
            n += 1
            if n == ROWS*COLS:
                return
            nexti = i + directions[d][0]
            nextj = j + directions[d][1]

            if nexti < 0 or nexti == ROWS or nextj < 0 or nextj == COLS or (nexti, nextj) in visited:
                d += 1
                d %= 4

            dfs(i + directions[d][0], j + directions[d][1])
        dfs(0, 0)

        return res
    

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # left to right : get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # top to bottom : get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break

            # right to left : get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # bottom to top : get every i in left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res



