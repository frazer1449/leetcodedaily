# Level: Medium, Topic: Graph

# Idea: Use a Union-Find Algorithm for Cycle Detection

# Path Compression, Union By Rank
# Rank: 1 (Highest), n (Lowest)
# map each node to its root.

from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)] # ith node -> parent (1 ~ n)
        rank = [1] * (N+1) # measures size of tree with root i

        # finds root node given previous edge data
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        # Given previous edge data,
        # returns True if n1, n2 not connected
        # returns False if n1, n2 connected
        # if not connected, connects based on new edge information
        # connect by setting pointer of smaller tree root to bigger tree root
        def union(n1, n2):
            # given previous information, we find roots of each
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                # we know that n1, n2 are connected
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]



