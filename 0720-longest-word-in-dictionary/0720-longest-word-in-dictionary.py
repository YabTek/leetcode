class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        ans = ""
        
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.isEndOfWord = True
            
        
        for word in words:
            cur = root
            
            for char in word:
                cur = cur.children[char]
                if not cur.isEndOfWord: break
            
            if cur.isEndOfWord and (len(word) > len(ans) or (len(word) == len(ans) and word < ans)):
                ans = word        
            
        return ans