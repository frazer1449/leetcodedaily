# House Robber II
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        return max(self.linearRob(nums[1:n]), nums[0] + self.linearRob(nums[2:n-1]))
    
    def linearRob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            
        