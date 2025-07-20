# 2D-DP : Coin Change II

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ROWS, COLS = len(coins), amount + 1
        memo = [[0] * COLS for _ in range(ROWS)]

        # row r : rth coin
        # col c : capacity c
        for c in range(COLS):
            memo[0][c] = 1 if c % coins[0] == 0 else 0
        
        for r in range(1, ROWS):
            for c in range(COLS):
                include = 0
                skip = memo[r-1][c]
                if c >= coins[r]:
                    include = memo[r][c-coins[r]]
                memo[r][c] = include + skip
                
        return memo[ROWS-1][COLS-1]