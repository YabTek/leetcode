class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        
    
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        
        for i, word in enumerate(words):
            self.addWord(i, word)
            
    def addWord(self, idx, word):
        
        for i in range(len(word)-1, -2, -1):
            newString = word[i+1:] + '#' + word
            cur = self.trie
            cur.idx = idx
            
            for char in newString:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                cur.idx = idx
        

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        newString = suff + '#' + pref
        
        for char in newString:
            if char not in cur.children:
                return -1
            cur = cur.children[char]
        
        return cur.idx
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)