# Remove Duplicates from Sorted Array II

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
# such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
                #l     r  
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

# l: point of interest pointer
# r: reading pointer

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        for r in range(2, n):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l

