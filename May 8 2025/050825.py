# Topic: Math & Geometry, Level: Easy
# Non-Cyclical Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        curr = n
        while curr != 1 and curr not in visited:
            visited.add(curr)
            curr = self.sos(curr)
        return (curr == 1)
        
    def sos(self, n: int) -> int:
        s = 0
        while n > 0:
            digit = n % 10
            s += digit * digit
            n = n // 10
        return s
