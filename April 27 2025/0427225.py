# Topic: Backtracking, Level: Medium
# Word Search

# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Key Ideas:
# starting dfs on row / column
# using a set() to track whether we repeat elements of a path
# storing current (r, c) and index i of 'word' we'll check

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # keep track of current (r, c) position, ith index of 'word' we are checking
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r,c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False