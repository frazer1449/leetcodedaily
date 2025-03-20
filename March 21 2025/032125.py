# Level: Medium, Topic: Binary Search

# Koko Eating Bananas

# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.

# Example 1:
# Input: piles = [1,4,3,2], h = 9
# Output: 2

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        # Eating Rate: between 1 and piles[-1] (size of largest pile) => Binary Search!
        l = 1
        r = piles[-1]
        stack = []
        while l <= r:
            m = (l + r) // 2
            t = Solution.minEatingTime(m, piles)
            if t > h:
                l = m + 1
            else:
                stack.append(m)
                r = m - 1
        
        if stack:
            return stack[-1]
    
    def minEatingTime(speed: int, piles: List[int]):
        t = 0
        for pile in piles:
            t += math.ceil(pile / speed)
        return t