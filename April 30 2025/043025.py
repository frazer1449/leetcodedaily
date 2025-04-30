# Topic: Trie, Level: Medium
# Prefix Trie

# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

# Implement the PrefixTree class:

# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# insert, search, startsWith functions

class TrieNode:
    def __init__(self):
        self.children = {} # char : TrieNode pairs
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.endOfWord = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.endOfWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True
