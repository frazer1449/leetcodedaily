# Heap / Priority Queue
# Two Heap (Advanced Algorithm)
# Find Median From Data Stream: use a 'small' maxHeap, 'large' minHeap

import heapq
class MedianFinder:

    def __init__(self):
        # small: maxHeap, large: minHeap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # need to satisfy invariant -self.small[0] < self.large[0]
        heapq.heappush(self.small, -num)
        if (self.small and self.large and -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # fix if size diff > 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        if len(self.small) > len(self.large):
            return (-self.small[0])
        if len(self.large) > len(self.small):
            return (self.large[0])
        
        