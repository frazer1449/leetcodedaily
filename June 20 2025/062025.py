# 1D-DP
# Coin Change

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount (at most 10000)
        # coins (at most 10)

        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-coin])

        return memo[amount] if memo[amount] != float("inf") else -1

