# 1-DP
# Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # i : index of interest
        # decode : past decoding
        def dfs(i: int):
            nonlocal ans

            if i == n:
                ans += 1
                return
            if s[i] != '0':
                dfs(i+1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                dfs(i+2)
        
        dfs(0)
        return ans