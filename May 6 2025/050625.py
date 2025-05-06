from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        # returns size of the island traverged at (r,c)
        def bfs(r, c) -> int:
            size = 0
            if grid[r][c] == 0:
                return 0

            direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            q = deque()
            grid[r][c] = 0
            q.append((r,c))

            while q:
                node = q.popleft()
                size += 1
                for dr, dc in direction:
                    nRow = node[0] + dr
                    nCol = node[1] + dc
                    if (nRow < 0 or nRow == ROWS or nCol < 0 or nCol == COLS
                    or grid[nRow][nCol] == 0):
                        continue
                    grid[nRow][nCol] = 0
                    q.append((nRow, nCol))
            return size
        
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, bfs(r,c))

        return ans
