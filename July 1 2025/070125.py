# Advanced Graphs
# Prim's Algorithm: Minimum Spanning Tree (very similar to Dijkstra)
# Step 1: Create a 'visited' set and 'minHeap' based on weight.
# Step 2: Choose a starting point, add it to 'visited' and add all edges to 'minHeap'
# Step 3: Pop from minHeap, add the edge to the mst, add all edges that go out from 
# new starting point to non-visited destinations

from typing import List
import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # n : number of vertices
        # edges : [src, dst, weight]

        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])
        
        # Initialize the heap by choosing a single node
        # and pushing all its neighbors
        minHeap = []
        for dst, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, dst])
        visited = set()
        visited.add(0)

        mst = []
        while minHeap and len(mst) < n-1:
            weight, src, dst = heapq.heappop(minHeap)
            if dst in visited:
                continue
            mst.append([src, dst, weight])
            visited.add(dst)
            for e, w in adj[dst]:
                if e in visited:
                    continue
                heapq.heappush(minHeap, [w, dst, e])
        if len(mst) != n - 1:
            return -1

        s = 0
        for src, dst, weight in mst:
            s += weight
        return s