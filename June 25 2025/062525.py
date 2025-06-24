# 1-Dimension DP
# Word Break: DP + Decision Tree

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solution: O(n * m) where n = len(s), m = len(wordDict)
        n = len(s)
        # stores whether splitting is possible from index i (1 or 0)
        cache = [-1] * n
        
        # i : current location
        # wordDict : list of words to check
        def memoization(i: int) -> int:
            # reached end: done
            if i == n:
                return True
            # already computed
            if cache[i] != -1:
                return (cache[i] == 1)
            for word in wordDict:
                m = len(word)
                if s[i:i+m] == word:
                    if memoization(i+m):
                        cache[i] = 1
                        return True
            cache[i] = 0
            return False
        
        return memoization(0)