class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Consider the Example:
        # i:      0  1  2  3  4
        # nums = [1, 3, 4, 2, 2]

        # Suppose we create nodes 0, 1, 2, 3, 4.
        # Connect directed graph / linked-list using edges i -> nums[i]
        #      2 -> 4 -> 2
        #.       ↖
        # 0 -> 1 -> 3

        # Use slow, fast pointer to find the point where slow & fast meet = pivot point
        # use trick of Floyd's Algorithm that says:
        # distance from starting point to cycle start = distance from pivot point to cycle start
        # think about why!

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow