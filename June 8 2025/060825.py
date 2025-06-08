# Greedy
# Jump Game
# This algorithm is greedy. We traverse from right to left and keep track of the goal (reachable) element closest to our right.

# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

# Input: nums = [1,2,0,1,0]

# Output: true
#                0 1 2 3 4
# Input: nums = [1,2,1,0,1]

# Output: false

from typing import List

class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        
        goal = n-1
        for i in range(n-2, -1, -1):
            if nums[i] >= goal - i:
                goal = i

        return goal == 0


print(Solution.canJump(nums = [1,2,0,1,0]))
print(Solution.canJump(nums = [1,2,1,0,1]))





