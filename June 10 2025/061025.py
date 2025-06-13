# Two Pointer
# Remove Duplicates From Sorted Array

# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# [1, 2, 3, 3, 3, 4, 4]

from typing import List

class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        while r < n:
            if nums[l] != nums[r]:
                l+=1
                nums[l] = nums[r]
            else:
                r+=1
        return l+1
    def removeDuplicatesTwo(nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[r] == nums[l]:
                r += 1
            l += 1
        return l
    

print(Solution.removeDuplicates([1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8]))


         

            
