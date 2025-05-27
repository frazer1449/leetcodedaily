# Task Scheduler
# Hybrid Usage of Max-Heap and timeQueue.

import heapq
from typing import List
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        timeQueue = deque()

        time = 0
        while maxHeap or timeQueue:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    timeQueue.append([cnt, time + n])
            
            if timeQueue and timeQueue[0][1] == time:
                heapq.heappush(maxHeap, timeQueue.popleft()[0])
        return time


