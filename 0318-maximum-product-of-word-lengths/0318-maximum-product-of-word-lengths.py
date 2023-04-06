class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = float("-inf")
        d = {}
        n = len(words)
        
        for word in words :
            binary = 0
            for char in word:
                binary |= (1<<(ord(char) - 97))
            d[word] = binary
            
            
        for i in range(n) :
            for j in range(i + 1 , n) :
                if d[words[i]] & d[words[j]] == 0 :
                    ans = max(ans , len(words[i] ) * len(words[j]))
                    
        if ans == float("-inf"):
            return 0
        else:
            return ans

        