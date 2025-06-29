# Advanced Graphs
# Kruskal's Algorithm: Min Cost to Connect Points

# You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

# Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        # Kruskal's Algorithm:
            # 1. Store all edges between any two points in "points" into 
            #    a heap with their distance
            # 2. For n-1 times, find the smallest distance edge, check that it doesn't create
            #    a cycle with UnionFind, then add it to 'mst' array.
        
        for i in range(n):
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                edges.append([distance, i, j])
        
        unionFind = UnionFind(n)
        heapq.heapify(edges)
        mst = []
        while len(mst) < n-1:
            dist, i, j = heapq.heappop(edges)
            if not unionFind.union(i, j):
                continue
            mst.append(dist)
        return sum(mst)

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True