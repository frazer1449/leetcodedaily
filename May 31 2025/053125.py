# 1 Dimension DP
# House Robber

# Bottom-Up DP
# rob[0:n] = max(arr[0] + rob[2:n], rob[1:n])

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # only need to store 2 previous values
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

