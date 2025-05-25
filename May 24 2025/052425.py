import heapq
from typing import List

# K Closest Points to Origin
# Lesson: heapify() function sorts list of lists lexicographically (starting with first elem)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ans = []

        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1:3])

        return ans
        


