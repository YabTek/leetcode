class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
     
        ans = 0
        start = len(questions)-2
        points = [0 for _ in range(start+2)]
        points[-1] = questions [-1][0]

        while start >= 0:    
            try:  
                idx = start+1+questions[start][1]
                end = questions[start][0] +points[idx]
                points[start] = max(end,points[start+1])

            except:
                end = questions[start][0] 
                points[start] = max(end,points[start+1])   
            start-=1
        ans = points[0]

        
        return ans