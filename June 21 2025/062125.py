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
        # Sort First O(nlogn)
        # Greedy Algorithm: In comparing two adjacent ones that overlap, keep the one that ends first O(n)
        
        # Sort based on starting point
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # non-overlapping
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res

print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4],[1,4]]))
print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4]]))
print(Solution.eraseOverlapIntervals(intervals = [[1,2],[2,4],[1,4], [4, 6], [5, 8]]))

        
        
        
        
        
        


                
    