# Level: Medium, Topic: Backtracking

# Combination Sum II
# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        # tracking:
        # 1. index i
        # 2. current array curr
        # 3. sum total

        # decision tree before index i = curr
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # include candidates[i]
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()

            #              i     i  i
            # [1, 1, 1, 1, 1, 2, 2, 3]
            # skip candidates[i] (to next batch of numbers)
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res
            