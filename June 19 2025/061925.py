class Solution:
    # Solution 1: DFS (Time Complexity: O(2^{m+n-2}))
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def dfs(x: int, y: int):
            nonlocal count
            if x == m or y == n:
                return
            if x == m-1 and y == n-1:
                count += 1
                return
            dfs(x+1, y)
            dfs(x, y+1)
        
        dfs(0,0)
        return count
    # Solution 2: Dynamic Programming (Memo)
    def uniquePaths2(m: int, n: int) -> int:
        # Time Complexity: O(m*n), Space Complexity: O(n)
        # while doing DFS we can use a cache.
        # start with bottom row
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]

print(Solution.uniquePaths2(3, 3))
        