# Topic: Graph, Level: Medium

# Pacific Water Flow 

# Key Idea: Start at the coastline and move uphill via multi-source BFS/DFS.
# Multi-Source DFS where we share the visited set, preventing overlap.

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit = set()
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or r == ROWS 
            or c < 0 or c == COLS 
            or (r, c) in visit or
            heights[r][c] < prevHeight
            ):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        return list(pac & atl)
        
        
                
            
