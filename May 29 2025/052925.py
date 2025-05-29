from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return 0
        if n == 2:
            return min(cost[0], cost[1])

        totalCostAtLocation = [0] * n
        
        # initial setting:
        totalCostAtLocation[n-1] = cost[n-1]
        totalCostAtLocation[n-2] = cost[n-2]

        for i in range(n-3, -1, -1):
            totalCostAtLocation[i] = cost[i] + min(totalCostAtLocation[i+1], totalCostAtLocation[i+2])
        
        return min(totalCostAtLocation[0], totalCostAtLocation[1])