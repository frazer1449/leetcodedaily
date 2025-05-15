# Topic: Graphs, Level: Medium

# Multi-Source BFS with lots of edge cases.

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i,j))
                elif grid[i][j] == 0:
                    grid[i][j] = -2
                else:
                    grid[i][j] = -1
        # empty cell: -2
        # fresh fruit: -1 (default)
        # rotten fruit: 0 (set by me)
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        minutes = 0
        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                if grid[nr][nc] == -1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
                    minutes = max(minutes, grid[nr][nc])

        for r in grid:
            if -1 in r:
                return -1

        return minutes
