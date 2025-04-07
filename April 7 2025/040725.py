# Topic: Bit Manipulation, Level: Easy

# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.
# You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

# Hint: Two Solutions. One uses O(n) memory and the other uses O(1) memory. 

# XOR operator: 0 ^ 0 = 0, 1 ^ 1 = 0, 0 ^ 1 = 1
# same => 0, diff => 1

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
            if hashMap[num] == 2:
                hashMap.pop(num)
        
        return list(hashMap.keys())[0]
    
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # store XOR result
        for n in nums:
            res = n ^ res
        return res
    
