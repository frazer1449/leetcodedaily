# Partition Equal Subset Sum

# You are given an array of positive integers nums.
# Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). 
# Otherwise, return false.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1, - 1, -1):
            newDp = dp.copy()
            for s in dp:
                newDp.add(s+nums[i])
            if target in newDp:
                return True
            dp = newDp
        return False