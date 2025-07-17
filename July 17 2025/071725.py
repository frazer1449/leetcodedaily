# Meeting Rooms II

# Definition of Interval:

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(count, res)
        return res
        


        