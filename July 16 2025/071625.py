# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
from typing import Optional, List

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode(0)
        minHeap = []
        # unique identifier to prevent comparison between ListNode objects directly
        count = 0
        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, count, node))
                count += 1

        pointer = root
        while minHeap:
            node = heapq.heappop(minHeap)[2]
            pointer.next = node
            pointer = node
            if node.next:
                heapq.heappush(minHeap, (node.next.val, count, node.next))
                count += 1
        
        return root.next