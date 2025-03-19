# Topic: Stack, Level: Medium

# Generate Parentheses
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        # backtrack: a function that helps traverse through a complicated maze where after meeting an endpoint it returns to a previous checkpoint
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res    
        
