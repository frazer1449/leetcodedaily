# Topic: Sliding Window, Difficulty: Medium

# Permutation in String
# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

# Example 1:
# Input: s1 = "abc", s2 = "lecabee"
# Output: true

# Example 2:
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt1 = self.count(s1)
        cnt2 = self.count(s2[:len(s1)])

        if cnt2 == cnt1:
            return True

        for i in range(len(s1), len(s2)):
            idx_remove = ord(s2[i - len(s1)]) - ord('a')  # char going out
            idx_add = ord(s2[i]) - ord('a')               # char coming in
            cnt2[idx_remove] -= 1
            cnt2[idx_add] += 1

            if cnt2 == cnt1:
                return True

        return False
        
    def count(self, s: str) -> List[int]:
        l = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            l[idx] += 1
        return l