# Advanced Graphs
# Dijkstra's Algorithm: Swim in Rising Water

# You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

# Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

# You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

# Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # At (x,y) we do the following actions:
            # 1. Pop [maxElevation, (x,y)] from minHeap
            # 2. For every adjacent position, add to minHeap with [newMaxElevation, (x+dx,y+dy)]
            # 3. This way, we can find the minimum max Elevation required to go from (0,0) to (x,y)
        
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        shortestTime = {} # stores (x,y) : maxElevation pairs

        minHeap = [(grid[0][0], (0, 0))]
        while minHeap:
            q = heapq.heappop(minHeap)
            if q[1] in shortestTime:
                continue
            shortestTime[q[1]] = q[0]

            x = q[1][0]
            y = q[1][1]
            for dx, dy in moves:
                if x+dx < 0 or x+dx == n or y+dy < 0 or y+dy == n:
                    continue
                if (x+dx, y+dy) not in shortestTime:
                    heapq.heappush(minHeap, (max(grid[x+dx][y+dy], q[0]),(x+dx, y+dy)))
        return shortestTime[(n-1, n-1)]



        
        