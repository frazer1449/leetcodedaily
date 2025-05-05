# Topic: Graphs, Level: Medium
# Number of Islands

# Sol 1: DFS

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = []
        for _ in range(ROWS):
            visited.append([0] * COLS)
        
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0" 
            or visited[r][c] == 1):
                return
            visited[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            
        
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c] == 0 and grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans

# Sol 2 : DFS (replace 1 with 0 when done)

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0"):
                return
            grid[r][c] == "0"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
                ans += 1
        return ans
    
# Sol 3: BFS
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            grid[r][c] == "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid[nr][nc] == "0"):
                        # continue means to end the for loop there.
                        continue
                    q.append(nr, nc)
                    grid[nr][nc] == "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

        
