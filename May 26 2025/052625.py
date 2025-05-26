# Climb Stairs
# 1-DP

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        for i in range(1, n+1):
            if (i == 1 or i == 2):
                memo[i] = i
            else:
                memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]