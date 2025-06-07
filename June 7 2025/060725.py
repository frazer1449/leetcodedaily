# 1-DP
# Palindroming Substrings

# Palindromic Substrings
# Given a string s, return the number of substrings within s that are palindromes.

# A palindrome is a string that reads the same forward and backward.

class Solution:
    @staticmethod
    def countSubstrings(s: str) -> int:
        n = len(s)
        ans = 0

        # odd length palindromes
        for i in range(n):
            j = 0
            while i + j < n and i - j >= 0 and s[i+j] == s[i-j]:
                ans += 1
                j+=1

        # even length palindromes
        for i in range(n-1):
            j = 0
            while i + 1 + j < n and i - j >= 0 and s[i+1+j] == s[i-j]:
                ans += 1
                j+=1
        
        return ans

print(Solution.countSubstrings("aaa"))

