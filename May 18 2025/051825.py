# Topic: Graph, Level: Medium

# Course Schedule

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS Algorithm and Updating!

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs) -> bool:
            # cycle detection
            if crs in visitSet:
                return False
            # if crs has no prerequisites, it's good
            if preMap[crs] == []:
                return True
            # if crs has prerequisites, we need to add it to the visitSet for backtracking
            visitSet.add(crs)

            # for all prerequisites, we check the validity of them
            for pre in preMap[crs]:
                # dfs(pre) call validates prerequisites, turns their map to []
                if not dfs(pre):
                    return False
            # reverse the backtracking
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
        


        


