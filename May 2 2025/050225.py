# Topic: Trie, Level: Hard

# Word Searcch II

# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

class TrieNode:
    def __init__(self):
        self.children = {} # value : TrieNode pair
        self.isWord = False
    
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, path = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 
            or r == ROWS or c == COLS 
            or (r,c) in path 
            or board[r][c] not in node.children):
                return
            
            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            path.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)