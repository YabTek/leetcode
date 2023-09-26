class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        ans = []
        n = len(words)
        
        for i, word in enumerate(words):
            words[i] = word.count(min(word))
            
        wordFreq = sorted(words)
        
        def moreThan(fQuery):
            low = 0
            high = n - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if wordFreq[mid] <= fQuery:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return n-low

        for query in queries:
            fQuery = query.count(min(query))
            temp = moreThan(fQuery)
            ans.append(temp)
            
        return ans






            
        