class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.keys.get(key, 0)
        
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            
            cur.value += diff
        self.keys[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
            
        return cur.value



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)