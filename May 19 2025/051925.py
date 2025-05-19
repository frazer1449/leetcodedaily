from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        edgeMap = {i: [] for i in range(n)}
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        visited = set()
        def dfs(curr, prev):
            # cycle detection
            if curr in visited:
                return False

            visited.add(curr)
            # for loop handles base case: leafs return True
            for neighbor in edgeMap[curr]:
                # prevent from going to prev node
                if neighbor == prev:
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True
        
        return dfs(0, -1) and (len(list(visited)) == n)
            