import heapq
from typing import List
# Last Stone Weight

# heapify(array): creates a minHeap for the array
# heappop():
# 1. pops upmost element 
# 2. puts minHeap[-1] into the top of array 
# 3. shifts down so that heap property is satisfied


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if (y > x):
                heapq.heappush(stones, x - y)

        return (0 if len(stones) == 0 else -stones[0])

