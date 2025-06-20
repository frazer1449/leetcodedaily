# Intervals
# Meeting Rooms

# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# determine if a person could add all meetings to their schedule without any conflicts.

# Input: intervals = [(0,30),(5,10),(15,20)]

# Output: false

# Input: intervals = [(5,8),(9,15)]

# Output: true

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(intervals: List[Interval]) -> bool:
        # Sort First O(nlogn)
        # Greedy Algorithm: In comparing two adjacent ones that overlap, keep the one that ends first
        
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

print(Solution.canAttendMeetings([(0,30),(5,10),(15,20)]))
print(Solution.canAttendMeetings([(5,8),(9,15)]))




