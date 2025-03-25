# Topic: Linked List, Level: Medium

# Remove Node From End of Linked List

# You are given the beginning of a linked list head, and an integer n.
# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:
# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        
        idx = cnt - n
        curr, prev = head, None
        num = 0
        while (num < idx):
            prev = curr
            curr = curr.next
            num += 1
        
        if num == 0:
            return head.next
        
        if prev:
            prev.next = curr.next
        
        return head
