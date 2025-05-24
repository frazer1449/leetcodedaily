import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k

        # Floyd's Heap Algorithm: O(n) complexity, but more than k elements
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            # (*) Genius Construction:
            # Explanation: Our minHeap has n elements. 
            # We pop n-k smallest ones to have the k biggest ones 
            # sorted from smallest to biggest. This way, we can pop the kth biggest one right away.
            heapq.heappop(self.minHeap)

    # My Code: Not most Efficient
    # def add(self, val: int) -> int:
    #     currentMin = self.minHeap[0]
    #     if (val < currentMin):
    #         return currentMin
    #     heapq.heappop(self.minHeap)
    #     heapq.heappush(self.minHeap, val)
    #     return self.minHeap[0]
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        