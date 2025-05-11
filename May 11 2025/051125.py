# Topic: Math & Geometry, Level: Easy
# Plus One

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # i : pivot index
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            i -= 1
        if i == -1:
            return [1] + [0]*len(digits)
        digits[i] += 1
        for j in range(i+1, len(digits)):
            digits[j] = 0
        return digits