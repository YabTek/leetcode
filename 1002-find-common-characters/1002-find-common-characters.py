class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = ""
        offset = ord('a')
        all_count = []

        
        for word in words:
            count = [0] * 26
            for char in word:
                idx = ord(char) - offset
                count[idx] += 1
            all_count.append(count)
            
        for idx,num in enumerate(zip(*all_count)):
            temp = set(num)
            temp = list(temp)
            if temp[0] == 1:
                ans += chr(idx+offset)
            elif temp[0] > 1:
                ans += temp[0] * chr(idx+offset)

        return ans
                    
                
            
    
            
        