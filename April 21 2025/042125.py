# Level: Medium, Topic: Backtracking
# Combination Sum

# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(arr, s, i):
            if s > target:
                return
            if s == target:
                res.append(arr)
                return
            # make sure the entries are mono increasing
            for j in range(i,n):
                dfs(arr + [nums[j]], s + nums[j], j)
        
        dfs([], 0, 0)
        return res