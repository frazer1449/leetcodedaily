# Topic: Binary Search, Level: Medium

# Search in Rotated Sorted Array

# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

# You may assume all elements in the sorted rotated array nums are unique,

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Find the Point of Inflection
        while (l < r):
            m = (l + r) // 2

            # if nums[m] lies in left sorted array
            if nums[m] > nums[r]:
                l = m + 1
            
            # if nums[m] lies in right sorted array
            else:
                # r = m can also be a possible inflection point
                r = m

        pivot = l

        # Binary Search on Left Sorted Array (index 0 ~ l - 1)
        l1 = 0
        r1 = pivot - 1
        while (l1 <= r1):
            m1 = (l1 + r1) // 2
            if nums[m1] == target:
                return m1
            elif nums[m1] > target:
                r1 = m1 - 1
            else:
                l1 = m1 + 1

        # Binary Search on Right Sorted Array (index l ~ len(nums) - 1)
        l2 = pivot
        r2 = len(nums) - 1
        while (l2 <= r2):
            m2 = (l2 + r2) // 2
            if nums[m2] == target:
                return m2
            elif nums[m2] > target:
                r2 = m2 - 1
            else:
                l2 = m2 + 1

        return -1

