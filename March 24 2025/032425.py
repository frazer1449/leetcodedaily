# Topic: Linked List, Level: Easy

############################## SOLUTION 1 w/ HASHSET ##############################

# Linked List Cycle Detection

# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        node = head
        while node:
            if node in visited.keys() and visited[node] == True:
                return True
            visited[node] = True
            node = node.next
        return False
    
############################## SOLUTION 2 w/ ALGORITHM ##############################

# Floyd's Tortoise & Hare Algorithm
# How It Works: 1 Slow Pointer s, 1 Fast Pointer f.
# Slow Pointer is shifted by 1, Fast Pointer is shifted by 2 (difference in speed)
# IF NO CYCLE: s, f do not meet
# IF CYCLE: s, f meet

class Solution: 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        # f reaches null.
        return False

