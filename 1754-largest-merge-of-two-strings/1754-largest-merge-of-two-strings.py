class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = ""
        
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                ans += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                ans += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    ans += word1[i]
                    i += 1
                else:
                    ans += word2[j]
                    j += 1
                
        ans += word1[i:]
        ans += word2[j:]
            
        return ans
                

        