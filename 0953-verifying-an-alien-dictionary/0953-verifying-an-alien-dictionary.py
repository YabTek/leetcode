class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = defaultdict(int)
        
        for idx,word in enumerate(order):
            d[word] = idx
       
        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first[:len(second)] == second:
                return False
            for x, y in zip(first, second):
                if d[x] > d[y]:
                    return False
                elif d[x] < d[y]:
                    break
                
        return True
        
        