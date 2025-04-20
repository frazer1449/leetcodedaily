# Topic: Backtracking, Level: Medium
# Subsets
# Given an array nums of unique integers, return all possible subsets of nums.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(curArr, i):
            # Decision Tree for ith index element of nums given curArr
            if i == n-1:
                res.append(curArr)
                res.append(curArr + [nums[i]])
                return
            dfs(curArr, i+1)
            dfs(curArr + [nums[i]], i+1)

        dfs([],0)
        return res