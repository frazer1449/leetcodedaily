# 2021. Brightest Position on Street

from typing import List

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        intervals = []
        for position, rng in lights:
            intervals.append([position - rng, position + rng])
        print(intervals)
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)

        res, count = 0, 0
        s, e = 0, 0
        ans = -float("inf")
        while s < len(intervals):
            if starts[s] <= ends[e]:
                count += 1
                if count > res:
                    res = count
                    ans = starts[s]
                s += 1
            else:
                count -= 1
                e += 1
        return ans