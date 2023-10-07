class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = [0]*len(words)
        root = TrieNode()
        
        for word in words:
            cur = root
            for char in word:
                cur = cur.children[char]
                cur.count += 1
        
        for i,word in enumerate(words):
            cur = root
            for char in word:
                cur = cur.children[char]
                ans[i] += cur.count
                
        return ans