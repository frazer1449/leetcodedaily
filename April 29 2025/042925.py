# Level: Medium, Topic: Backtracking
# Letter Combinations of a Phone Number

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashMap = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"],
        6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        
        if not digits:
            return []

        def dfs(curr: str, i: int):
            if i == len(digits):
                res.append(curr)
                return
            
            digit = int(digits[i])
            for letter in hashMap[digit]:
                dfs(curr + letter, i+1)
            
        
        dfs("", 0)
        return res