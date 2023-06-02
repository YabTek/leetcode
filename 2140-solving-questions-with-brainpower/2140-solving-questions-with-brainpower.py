class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        d = {}
        def dp(idx):
            
            if idx in d:
                return d[idx]
            if idx == len(questions)-1:
                return questions[idx][0]
            if idx >= len(questions):
                return 0
            
            d[idx] = max(questions[idx][0]+dp(idx+questions[idx][1]+1),dp(idx+1))
            return d[idx]
                
            
        return dp(0)
        