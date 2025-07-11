# N-Queens
# Backtracking: Permutations + Diagonals
# Key Idea: For Diagonals, use a "r+c" and "r-c" hashset to check duplicates.

from typing import List

class Solution:
    def __init__(self):
        self.me = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # checks for r + c duplicates
        negDiag = set() # c hecks for r - c duplicates

        res = []
        board = [["."]*n for i in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            # testing all columns for a row r
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

print(Solution().solveNQueens(n=4))
