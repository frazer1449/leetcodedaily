from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        L = 0
        maxLength = 1

        # invariant: L + 1 <= R
        for R in range(1, len(arr)):
            # return 0 if arr[R] == arr[R-1]
            # return 1 if arr[R] > arr[R-1]
            # return -1 if arr[R] < arr[R-1]
            comp = (arr[R] > arr[R-1]) - (arr[R] < arr[R-1])

            if comp == 0:
                L = R
                continue
            if R < len(arr)-1:
                nextComp = (arr[R+1] > arr[R]) - (arr[R+1] < arr[R])
                if (comp)*(nextComp) != -1:
                    # streak ends at R. update maxLength
                    maxLength = max(maxLength, R - L + 1)
                    L = R
        # check last turbulent window
        maxLength = max(maxLength, R - L + 1)

        return maxLength