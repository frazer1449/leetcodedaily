from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i:[] for i in range(n)}
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neighbor in edgeMap[i]:
                dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count