class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        ans = []
       
        for start,end,direction in shifts:
            if direction == 0:
                if end < len(s)-1:
                    prefix[start] += -1
                    prefix[end+1] += 1
                else:
                     prefix[start] += -1
            else:
                if end < len(s)-1:
                    prefix[start] += 1
                    prefix[end+1] += -1
                else:
                     prefix[start] += 1
                        
        for i in range(len(prefix)-1):
            prefix[i+1] += prefix[i]
            
        for i in range(len(s)):
            temp = prefix[i] + ord(s[i]) - 97
            temp %= 26
            temp += 97
            ans.append(chr(temp))
                 
        return "".join(ans)
                    
                    
                
            