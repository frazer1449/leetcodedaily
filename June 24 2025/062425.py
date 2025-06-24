# Sliding Window (Variable Size)
# Minimum Window Substring 

# Given two strings s and t, return the shortest substring of s such that every character in t, 
# including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tComp = dict(Counter(t))
        curWindow = {}
        ans = "0" * 10000

        def contains(p: dict, q: dict):
            for c in q:
                if p.get(c, 0) < q[c]:
                    return False
            return True

        L = 0
        # find the best one that ends at R
        for R in range(len(s)):
            curWindow[s[R]] = curWindow.get(s[R], 0) + 1
            while contains(curWindow, tComp):
                if len(ans) > (R - L + 1):
                    ans = s[L:R+1]
                curWindow[s[L]] -= 1
                L += 1
        
        return "" if ans == "0" * 10000 else ans