# Greedy

# Jump Game II

# You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].

# Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.
                #2 1 3 2 1 0
# i : position
# Input: nums = [2,4,1,1,1,1]

# Output: 2

# Input: nums = [2,1,2,1,0]

# Output: 2
from typing import List

class Solution:
    @staticmethod
    def jumpOfficial(nums: List[int]) -> int:
        res = 0
        l = r = 0

        # while r != last
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res

    @staticmethod
    def jump(nums: List[int]) -> int:
        n = len(nums)

        # memo: stores the minimum jumps to index n-1 from index i.
        memo = [float("inf")] * n
        if n == 1:
            return 0
        
        memo[n-1] = 0
        for i in range(n-2, -1, -1):
            maxJump = nums[i]
            if maxJump == 0:
                continue
            memo[i] = 1+min(memo[i+1:i+maxJump+1])

        return memo[0]
    
from datetime import datetime
                
print(Solution.jump(nums = [2,4,1,1,1,1]))
print(Solution.jump(nums = [2,1,2,1,0]))
print(Solution.jump(nums = [1, 0, 3]))
print(Solution.jump(nums = [2, 4, 5, 1, 1, 1, 1, 0, 1, 1]))



            
                

            
        