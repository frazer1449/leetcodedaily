# Intervals
# Merge Intervals

# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, 
# but [1, 2] and [2, 3] are overlapping.

# Input: intervals = [[1,3],[1,5],[6,7]]

# Output: [[1,5],[6,7]]

# Input: intervals = [[1,2],[2,3]]

# Output: [[1,3]]

# O(nlogn) , O(n) space

# We first sort (first on first element, second on second element)
from typing import List

class Solution:
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        # Time Complexity: nlogn
        intervals = sorted(intervals)

        res = []
        n = len(intervals)
        
        # Time Complexity: n
        mergeInterval = intervals[0]
        for i in range(1, n):
            if mergeInterval[1] < intervals[i][0]:
                res.append(mergeInterval)
                mergeInterval = intervals[i]
                continue
            mergeInterval[0] = min(mergeInterval[0], intervals[i][0])
            mergeInterval[1] = max(mergeInterval[1], intervals[i][1])
        res.append(mergeInterval)
        
        return res

print(Solution.merge(intervals = [[1,3],[1,5],[6,7]]))
print(Solution.merge(intervals = [[1,2],[2,3]]))
print(Solution.merge(intervals = [[1,3],[1,5], [2,5], [6,7], [7, 9], [8,10], [11,12]]))
            

# However, it's not guaranteed that they are sorted.
print(sorted([[1,3],[8,10], [2,5], [6,7], [11,12],[1,5], [7, 9]]))
