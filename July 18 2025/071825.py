# Partition Labels
# You are given a string s consisting of lowercase english letters.
# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.
# Return a list of integers representing the size of these substrings in the order they appear in the string.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # "xyxxyzbzbbisl"
        intervals = {}
        for i in range(len(s)):
            if s[i] not in intervals:
                intervals[s[i]] = [i, i]
                continue
            intervals[s[i]][1] = i
        
        ans = []
        
        start, end = 0, 0
        t = 0
        while t < len(s):
            end = max(end, intervals[s[t]][1])
            if t == end:
                ans.append(end - start + 1)
                start, end = end+1, end+1
            t+=1
        return ans