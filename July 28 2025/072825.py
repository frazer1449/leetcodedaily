# 1743. Restore the Array From Adjacent Pairs

from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        degrees = defaultdict(int)

        for u, v in adjacentPairs:
            edges[u].append(v)
            edges[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        start = None
        for v in degrees:
            if degrees[v] == 1:
                start = v
        
        ans = []
        prev = None
        cur = start
        while True:
            ans.append(cur)
            nxts = edges[cur]
            nxt = nxts[0] if len(nxts) == 1 or nxts[0] != prev else nxts[1]
            if len(ans) == len(degrees):
                break
            prev, cur = cur, nxt
        return ans

        return ans