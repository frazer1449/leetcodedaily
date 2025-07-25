# 992. Subarrays with K Different Integers

from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def slidingWindowAtMost(nums, k):
            freq = {}
            l = totalCount = 0
            for r in range(len(nums)):
                if nums[r] not in freq:
                    freq[nums[r]] = 0
                freq[nums[r]] += 1

                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                totalCount += (r - l + 1)
            return totalCount
        
        return slidingWindowAtMost(nums, k) - slidingWindowAtMost(nums, k-1)