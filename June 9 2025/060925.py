# Minimum Size Subarray Sum
# Sliding Window Variable Size

# You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        L, total = 0, 0
        minLength = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLength = min(minLength, R-L+1)
                total-=nums[L]
                L+=1
        return 0 if minLength == float("inf") else minLength
                
