# Longest Increasing Subsequence
# 1-DP & DFS (Complexities: O(n^2), O(2^n))

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".

# Input: nums = [9,1,4,2,3,3,7]

# Output: 4

# Input: nums = [0,3,1,3,2,3]

# Output: 4

from typing import List

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        curr = []
        def dfs(i):
            nonlocal ans
            if i == len(nums):
                ans = max(ans, len(curr))
                return
            # skip ith element
            dfs(i+1)
            
            # attach ith element
            if not curr or nums[i] > curr[-1]:
                curr.append(nums[i])
                dfs(i+1)
                curr.pop()
        dfs(0)
        return ans

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        memo = [1] * n

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1+memo[j])
        return max(memo)


