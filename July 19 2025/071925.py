# 0 / 1 Knapsack

from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        memo = [[0] * COLS for i in range(ROWS)]
        
        # first row
        for c in range(COLS):
            memo[0][c] = profit[0] if weight[0] <= c else 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                include = -1
                skip = memo[r-1][c]
                if c-weight[r] >= 0:
                    include = profit[r] + memo[r-1][c-weight[r]]
                memo[r][c] = max(include, skip)
        
        return memo[ROWS-1][COLS-1]


