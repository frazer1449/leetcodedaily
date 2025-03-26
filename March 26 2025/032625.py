# Level: Medium, Topic: Binary Search

# Find Minimum in Rotated Sorted Array

# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example:
# Input: nums = [3,4,5,6,1,2]
# Output: 1

from typing import List

# Key Ideas in Problem: 
# if completely sorted array, return left element
# if nums[m] >= nums[r] => part of left sorted array, if nums[m] < nums[r] => part of right sorted array
# check res = min(res, nums[m]) whenever nums[m] has chance of being pivot

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1

        # Consider Example: [3, 4, 5, 1, 2]
        while (l <= r):
            # if sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            # If we are in the left sorted array (ex. [3, 4, 5]), 
            # middle element > left element
            # search right
            if nums[m] >= nums[l]:
                l = m + 1
            # If we are in the right sorted array (ex. [1, 2]), 
            # middle element < left element
            # search left
            elif nums[m] < nums[l]:
                r = m - 1
        return res