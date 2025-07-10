# Permutations II
# Backtracking: Permutations

# You are given an array nums, that might contain duplicates , return all possible unique permutations in any order.

# Input: nums = [1,1,2]

# Output: [
#     [1,1,2],
#     [1,2,1],
#     [2,1,1]
# ]

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for n in count:
                if count[n] > 0:
                    curr.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    curr.pop()
        dfs()
        return res