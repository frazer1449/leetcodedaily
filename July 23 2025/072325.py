# 3043. Find the Length of the Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashSet = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                hashSet.add(s[:i])
        
        ans = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in hashSet:
                    ans = max(ans, i)
        return ans