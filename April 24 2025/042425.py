# Level: Medium, Topic: Backtracking
# Subsets II


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            # include nums[i]
            curr.append(nums[i])
            backtrack(curr, i+1)
            curr.pop()

            # skip nums[i] (and similar elements)
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(curr, i+1)

        backtrack([], 0)
        return res