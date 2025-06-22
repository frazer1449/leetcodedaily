# Greedy
# Valid String with Wild Card *

from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Due to the variable *, we keep the range of possible leftMin, leftMax.
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                # we shouldn't artificially force leftMin to be negative
                leftMin, leftMax = max(0, leftMin - 1), leftMax + 1
            if leftMax < 0:
                return False
        return True if leftMin <= 0 and leftMax >= 0 else False