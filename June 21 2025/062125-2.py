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
        intervals = sorted(intervals, key=lambda x: x.start)
        n = len(intervals)
        for i in range(n-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True

def createInterval(list: List[tuple]) -> List[Interval]:
    intervals = []
    for interval in list:
        intervals.append(Interval(interval[0], interval[1]))
    return intervals

print(Solution.canAttendMeetings(createInterval([(0,30),(5,10),(15,20)])))
print(Solution.canAttendMeetings(createInterval([(5,8),(9,15)])))




