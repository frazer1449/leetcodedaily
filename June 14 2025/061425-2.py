# Greedy
# Gas Station

# There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

# gas[i] is the amount of gas at the ith station.
# cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
# You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

# It's guaranteed that at most one solution exists.


''' Thoughts
# Station 3: +4 (total 4)
# 3 -> 0: -1 (total 3)
# Station 0: +1 (total 4)
# 0 -> 1: -2 (total 2)
# Station 1: +2 (total 4)
# 1 -> 2: -2 (total 2)
# Station 2: +3 (total 5)
# 2 -> 3: -4 (total 1)

# gas at station i, go to station i+1 = [1-2, 2-2, 3-4, 4-1] = [-1, 0, -1, 3]
'''

# Input: gas = [1,2,3,4], cost = [2,2,4,1]
# Output: 3

# Input: gas = [1,2,3], cost = [2,3,2]

# Output: -1

# Think of gas and cost as hills and valleys:
# If the total elevation gain (gas) is more than the total descent (cost), then somewhere on this circular terrain, 
# there’s a “valley” low enough to start your journey and make it all the way around without ever going below sea level.

# Brute Force: O(n^2)
# Greedy: O(n)

from typing import List

class Solution:
    @staticmethod
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        # solution exists if and only if 
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1
        return start
        # guaranteed that one of the starts would work
        
        
    
print(Solution.canCompleteCircuit(gas = [1,2,3,4], cost = [2,2,4,1]))
print(Solution.canCompleteCircuit(gas = [1,2,3], cost = [2,3,2]))