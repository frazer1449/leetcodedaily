# Sliding Window Fixed Variable
# Contains Duplicate II
# Idea: Sliding Window of Size k using hashSet.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # windows of size k+1 (abs(i-j)<=k)
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
