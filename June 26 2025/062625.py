# Advanced Graphs
# Dijkstra's Algorithm: Network Delay Time

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency hashMap
        adj = {}
        
        # filling in adjacency information
            # ui: start
            # vi: destination
            # ti: time (weight)
        for i in range(1, n+1):
            adj[i] = []
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in shortest:
                continue
            shortest[v1] = t1

            for v2, t2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, v2))

        return max(shortest.values()) if len(shortest) == n else -1
        

        
