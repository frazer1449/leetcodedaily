# Alien Dictionary
# Advanced Graphs (Topological Sort)

# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # If we can build the graph, we can finish the problem via topological sort.
        # To build the graph, we only need to compare adjacent inputs.

        # Step 1: Build Adjacency List
        adj = {}
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = []

        # Step 2: Compare Adjacent Edges
        n = len(words)
        for i in range(n-1):
            w1 = list(words[i])
            w2 = list(words[i+1])
            mismatch_found = False
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    mismatch_found = True
                    # stop comparing after first mismatch
                    break
                j+=1
            if not mismatch_found and len(w1) > len(w2):
                return ""
        
        # Step 3: Perform Topological Sort on 'adj'
        # reverse order topSort. at end, do topSort.reverse()
        topSort = []
        # visit : permanent marking (if all children in visit, we can add to topSort)
        visit = set()
        # cycle detection
        path = set()

        def dfs(src):
            if src in path:
                # cycle detected!
                return False
            if src in visit:
                return True
            visit.add(src)

            path.add(src)
            for dst in adj[src]:
                # runs dfs(dst) while returning whether there is a cycle or not.
                if not dfs(dst):
                    return False
            path.remove(src)
            topSort.append(src)
            return True
        
        for node in adj:
            if not dfs(node):
                return ""
        topSort.reverse()

        return "".join(topSort)