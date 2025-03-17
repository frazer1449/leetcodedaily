# Topic: Stack, Level: Medium

# Daily Temperatures
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

# Example 2:
# Input: temperatures = [22,21,20]
# Output: [0,0,0]

from typing import List

class Solution:
    # Thoughts:
    # 1. Iterate through the "temperatures" list. For each index i, temperature t combination, determine if the current combination has a higher temperature than ones in the stack.
    # 2. Pop all elements in the stack that have lower temperature than current chosen one.
    # 3. Add element i into the stack.
    # 4. Ending entries are assigned a result of 0.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        # Iteration
        for i, t in enumerate(temperatures):

            # Popping
            while stack and stack[-1][0] < t:
                previ = stack.pop()[1]
                res[previ] = i - previ
            # Adding Element i
            stack.append((t,i))
        
        # Dealing with Final Cases
        # res: already initialized with 0s
        # stack: pop remaining elements (because why not?)
        while stack:
            stack.pop()
        
        return res