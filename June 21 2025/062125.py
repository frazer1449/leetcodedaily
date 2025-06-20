# Intervals
# Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

# Input: intervals = [[1,2],[2,4],[1,4]]

# Output: 1

# Input: intervals = [[1,2],[2,4]]

# Output: 0

# Idea: Treat each interval as a vertex. If two intervals are overlapping, connect them with an edge.

from typing import List

class Solution:
    def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
        n = len(intervals)
        # i : degree ((i+1)th interval & its degree) / note: i ranges from 0 ~ n-1
        edges = {i:[] for i in range(n)}
        degrees = {i:0 for i in range(n)}

        for i in range(n):
            for j in range(i+1, n):
                if intervals[i][0] > intervals[j][1] or intervals[i][1] > intervals[j][0]:
                    edges[i].append(j)
                    edges[j].append(i)
                    degrees[i]+=1
                    degrees[j]+=1
        print(edges)
        
        count = 0
        while True:
            i = findMaximumIdx(list(degrees.values()))
            if i == -1:
                break
            for v in edges[i]:
                edges[v].remove(i)
                degrees[v] -= 1
            edges[i] = []
            degrees[i] = 0
            count += 1
        
        return count

def findMaximumIdx(list) -> int:
    idx = -1
    mx = 0
    for i in range(len(list)):
        if list[i] > mx:
            mx = list[i]
            idx = i
    return idx

print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4],[1,4]]))
print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4]]))
print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4],[1,4], [4, 6], [5, 8]]))

        
        
        
        
        
        


                
    