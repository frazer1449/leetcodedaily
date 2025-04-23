# Level: Medium, Topic: Backtracking

# Permutations
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        pick = [False] * n

        def dfs(curr):
            nonlocal nums, pick

            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(curr)
                    curr.pop()
                    pick[i] = False
        
        dfs([])
        return res