from typing import List

# Kadane's Algorithm with Circular Array
# Q: How can we find the maximum contiguous subarray given a circular array?
# A: Key Idea is to actually find the MINIMUM CONTIGUOUS SUBARRAY because it's complement would naturally be the maximum contiguous subarray
# contiguous subarray + complement contiguous subarray = fixed sum
# a contiguous subarray & its complement cannot both cross the [n-1, 0] border. maximum contiguous subarray either is going to be the
# maximum linear contiguous subarray or total sum - minimum linear contiguous subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # find the linear global max & global min (don't consider circular)
        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for n in nums:
            total+= n

            curMax = max(0, curMax)
            curMin = min(0, curMin)

            curMax += n
            curMin += n

            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        # all negative
        if globalMax < 0:
            return globalMax
        
        return max(globalMax, total - globalMin)