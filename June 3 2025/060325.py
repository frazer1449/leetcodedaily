# Kadane's Algorithm
# Q: Find the maximum contiguous subarray.
# A: Key Idea is to notice that the maximum subarray ending at i is either (maxSub at i-1 + arr[i] OR arr[i])
# depending on whether maxSub at i-1 is negative.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Idea: traverse through array and find largest contiguous array ending at i
        # this depends on whether the largest contiguous array ending at i-1 sums negative
        maxSum = nums[0]
        currSum = 0

        for i in range(len(nums)):
            # currSum = sum of largest contiguous array (i-1)
            currSum = max(0, currSum)
            # currSum = sum of largest contiguous array i
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
        
        return maxSum