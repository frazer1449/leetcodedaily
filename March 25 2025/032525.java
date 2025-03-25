// Reorder Linked List
// You are given the head of a singly linked-list.
// The positions of a linked list of length = 7 for example, can intially be represented as:
// [0, 1, 2, 3, 4, 5, 6]
// Reorder the nodes of the linked list to be in the following order:
// [0, 6, 1, 5, 2, 4, 3]
// Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
// [0, n-1, 1, n-2, 2, n-3, ...]
// You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

public class ListNode{
    int val;

    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public void reorderList(ListNode head) {
        // find middle 
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        // reverse second half
        ListNode second = slow.next;
        slow.next = null;
        ListNode prev = null;
        while (second != null){
            ListNode tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        }

        // merge two halfs
        ListNode first = head;
        second = prev;

        while (second != null){
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;
            first.next = second;
            second.next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
}
