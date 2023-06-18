class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        
        for a,b in items1:
            d[a] = b
            
        for a,b in items2:
            if a not in d:
                d[a] = b
            else:
                d[a] += b
            
        return sorted(d.items())
        

