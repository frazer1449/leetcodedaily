# Advanced Graphs
# Dijkstra's Algorithm (while tracking cost and # edges)
# Cheapest Flights Within K Stops

# There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.

# You are also given three integers src, dst, and k where:

#   src is the starting airport
#   dst is the destination airport
#   src != dst
#   k is the maximum number of stops you can make (not including src and dst)
# Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.

# Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

# Output: 500

# Input: n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1

# Output: 200

from typing import List
import heapq

class Solution:
    def __init__(self):
        return
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Create Adjacency List
        adj = {}
        for i in range(n):
            adj[i] = []
        for f, t, p in flights:
            # f: from, t: to, p: price (directed edges)
            adj[f].append([t, p])
        
        # Step 2: MinHeap: [price, stops, node]
        minHeap = [[0, 0, src]]  # price, stops, node

        while minHeap:
            price, stops, node = heapq.heappop(minHeap)
            if stops > k+1:
                continue
            if node == dst:
                return price
            for t, p in adj[node]:
                heapq.heappush(minHeap, [price + p, stops + 1, t])
                
        return -1


print(Solution().findCheapestPrice(n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1))
print(Solution().findCheapestPrice(n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1))


