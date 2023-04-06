class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        store = set()
        nodes = set([i for i in range(n)])
        
        for a,b in edges:
            store.add(b)
            
        return nodes-store
        
            
