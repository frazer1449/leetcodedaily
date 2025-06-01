# Longest Palindrome
# Lesson: Start at the middle and expand outwards
# 1-DP

# Time Complexity: O(n^2) (double for-loop)
# Space Complexity: O(1) (we don't really store anything)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        # odd length palindromes
        for i in range(len(s)):
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i+j] == s[i-j]:
                j += 1
            if len(longest) < 2*j -1:
                longest = s[i-j+1:i+j]
        
        # even length palindromes
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                continue
            j = 1
            while i - j >= 0 and i + 1 + j < len(s) and s[i-j] == s[i+j+1]:
                j+=1
            if len(longest) < 2*j:
                longest = s[i-j+1:i+j+1]
        return longest
            
                