# 2. Add Two Numbers
# Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1, p2 = l1, l2
        root = ListNode(0, None)
        prev = root
        while p1 and p2:
            prev.next = ListNode((p1.val + p2.val + carry) % 10, None)
            carry = (p1.val + p2.val + carry) // 10
            prev = prev.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            prev.next = ListNode((p1.val + carry) % 10, None)
            carry = (p1.val + carry) // 10
            prev = prev.next
            p1 = p1.next
        
        while p2:
            prev.next = ListNode((p2.val + carry) % 10, None)
            carry = (p2.val + carry) // 10
            prev = prev.next
            p2 = p2.next
        
        if carry:
            prev.next = ListNode(1, None)
            carry = 0

        return root.next