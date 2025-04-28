# Topic: Backtracking, Level: Medium

# Palindrome Partitioning
# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
# You may return the solution in any order.

# Key Ideas:
# check palindrome by s[i:j+1] == s[i:j+1][::-1]

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # curr : previously completed partition
        # i : starting index of palindrome we'll observing
        def dfs(curr, i):
            if i == len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    dfs(curr, j+1)
                    curr.pop()
            
        dfs([], 0)
        return res