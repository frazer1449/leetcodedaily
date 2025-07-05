# Math & Geometry
# Counting Squares (Key Idea: Use Diagonal Points to Find Squares)

from typing import List

class CountSquares:

    def __init__(self):
        self.stream = {}
        

    def add(self, point: List[int]) -> None:
        point = (point[0], point[1])
        if point not in self.stream:
            self.stream[point] = 0
        self.stream[point] += 1
        
    def count(self, point: List[int]) -> int:
        point = tuple(point)
        def isDiagonal(p1, p2):
            difx = p1[0] - p2[0]
            dify = p1[1] - p2[1]
            if abs(difx) == abs(dify) and p1 != p2:
                return True
            return False
        ans = 0
        for p in self.stream:
            if isDiagonal(point, p):
                if (point[0], p[1]) in self.stream and (p[0], point[1]) in self.stream:
                    ans += self.stream[p] * self.stream[(point[0], p[1])] * self.stream[(p[0], point[1])]
        return ans