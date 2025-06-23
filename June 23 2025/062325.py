# 2-Dimension DP
# Unique Paths II

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * (10^9).

from typing import List

class Solution:
    # Top-Down Solution
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = [[0] * cols for i in range(rows)]

        def memoization(r, c, rows, cols, cache):
            # check if out of bounds or blocked by obstacle
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            # check if problem has been already solved before
            if cache[r][c] > 0:
                return cache[r][c]
            # check if we are at the end
            if r == rows - 1 and c == cols - 1:
                return 1
            
            # generate answer and save to cache
            cache[r][c] = (memoization(r+1, c, rows, cols, cache) + 
            memoization(r, c+1, rows, cols, cache))


            return cache[r][c]
        
        return memoization(0, 0, rows, cols, cache)
    # Down-Up Solution
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        prevRow = [0] * cols
        for i in range(rows - 1, -1, -1):
            curRow = [0] * cols
            for j in range(cols - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    curRow[j] = 0
                elif i == rows - 1 and j == cols - 1:
                    curRow[j] = 1
                else:
                    right = curRow[j+1] if j + 1 < cols else 0
                    down = prevRow[j]
                    curRow[j] = right + down
            prevRow = curRow
        return prevRow[0]

            
