# Topic: Graphs, Level: Medium

# Islands and Treasures

# Islands and Treasures is a problem where there is a grid with each r, c entry either
# water (unwalkable), land, or treasure. For each land coordinate, we want to write on it the shortest length to a treasure box.
# To do that, we first collect all the treasure coordinates into a queue. Then, we will perform pseudo-BFS on the elements of the queue
# land coordinates are updated and added to the queue if and only if its the first time its discovered.

# The reason why this works is that the queue initially collects all coordinates that have distance 0 to the box.
#  Then the queue collects all coordinates distance 1 to the box... and so on, which makes sure the number written on the coordinates is minimal.

from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:  # treasure chest
                    queue.append((r, c))
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            r, c = queue.popleft()
            print(r, c)
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        
            
