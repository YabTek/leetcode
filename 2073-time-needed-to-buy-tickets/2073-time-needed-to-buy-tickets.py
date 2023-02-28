class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()
        ans = 0
        
        for i in range(len(tickets)):
            que.append([tickets[i],i])
     
        while que:
            front = que.popleft()
            if front[0] > 0:
                front[0] -= 1
                ans += 1
                if front[0] == 0 and front[1] == k :
                    break
            que.append([front[0],front[1]]) 
         
        return ans
                    

       
