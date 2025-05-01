# Topic: Trie, Level: Medium

# Design Add and Search Word Data Structure

# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode:
    def __init__(self):
        self.children = {} # char : TrieNode pairs
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i+1)
        return dfs(self.root, 0)

