from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create Adjacency List
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        # Step 2: Construct DFS
        topSort = []
        visit = set()
        path = set()
        def dfs(src):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            
            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            path.remove(src)

            topSort.append(src)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort
            