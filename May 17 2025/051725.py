# Surrounded Regions

# Replace regions of Os that are surrounded with Xs (not connected to border)
# Idea: Multi-source DFS from border Os.

# Topic: Graph, Level: Medium

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        visited = set()
        def dfs(r, c):
            if (r < 0 or r == ROWS or
             c < 0 or c == COLS or
            board[r][c] == "X" or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    if board[r][c] == "O":
                        dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        