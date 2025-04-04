# Implement the RandomizedSet class that can do the following
# - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

from collections.abc import ValuesView
import random

class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.list = []
        self.map = {}
    
    def insert(self, val) -> bool:
        s = self.set
        l = self.list
        m = self.map
        if val in s:
            return False
        s.add(val)
        l.append(val)
        m[val] = len(l) - 1
        return True

    def remove(self,val) -> bool:
        s = self.set
        l = self.list
        m = self.map
        if val not in s:
            return False
        s.remove(val)
        i = m[val]
        last = l[-1]

        # update list (swap & pop)
        l[i] = last
        l[-1] = val
        l.pop()

        # update map
        m[last] = i
        m.pop(val)
        
        return True
    
    def getRandom(self) -> int:
        l = self.list
        return random.choice(l)

rset = RandomizedSet()
rset.insert(4)
rset.insert(1)
rset.insert(10)
rset.insert(5)
rset.insert(6)
rset.remove(10)

output = []
for i in range(15):
    x = rset.getRandom()
    output.append(x)

print(output)