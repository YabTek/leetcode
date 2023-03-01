class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        count = Counter(s)
        visited = {}
        
        for char in count:
            visited[char] = False
      
        for char in s:
            while stk and char < stk[-1] and count[stk[-1]] > 0 and visited[char] == False:
                cur = stk.pop()
                visited[cur] = False
                
            if  count[char] > 0 and visited[char] == False:
                stk.append(char)
                visited[char] = True
            count[char] -= 1
            
        return "".join(stk)
                
            
        
        
        