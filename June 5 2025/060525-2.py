# Sliding Window Fixed Variable
# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

from typing import List

class Solution:
    @staticmethod
    def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        n = len(arr)
        L = 0
        sum = 0
        
        N = k * threshold

        for R in range(n):
            # we shrink if R - L + 1 > k <-> R - L + 1 >= k+1 <-> R - L >= k
            if R - L >= k:
                sum -= arr[L]
                L += 1
            sum += arr[R]
            if sum >= N and R-L+1 == k:
                ans += 1
        
        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)


print(Solution.numOfSubarrays(arr=[2,2,2,2,5,5,5,8], k=3, threshold=4))
print(Solution.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))