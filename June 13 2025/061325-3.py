# Arrays: Prefix SUms
# Subarray Sum Equals K

# You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [2,-1,1,2], k = 2

# Output: 4

# Input: nums = [4,4,4,4,4,4], k = 4

# Output: 6

from typing import List

class Solution:
    def subarraySum(nums: List[int], k: int) -> int:
        prefix = {0 : 1}

        ans = 0
        currSum = 0
        for n in nums:
            currSum += n
            if currSum - k in prefix:
                ans += prefix[currSum - k]
            if currSum not in prefix:
                prefix[currSum] = 0
            prefix[currSum] += 1
        return ans

print(Solution.subarraySum(nums = [2,-1,1,2], k = 2))
print(Solution.subarraySum(nums = [4,4,4,4,4,4], k = 4))


        
            
