class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        indices = defaultdict(list)  
        
        def check(word):
            i = -1  
            
            for char in word:
                if char not in indices:
                    return False
                possible_indices = indices[char]
                
                new_index = bisect.bisect_left(possible_indices, i+1)
                if new_index == len(possible_indices):
                    return False
                i = possible_indices[new_index]
            return True

        
       
        for i, char in enumerate(s):
            indices[char].append(i)
        
  
        for word in words:
            if check(word):
                ans += 1
        
        return  ans