class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        total = 0
        new_cost = sorted(costs, key=lambda x: (x[0] - x[1]))
        
        for num in new_cost[:n//2]:
            total += num[0]
            
        for num in new_cost[n//2:]:
            total += num[1]
       
        
        return total
        
        
       
    
    
        
       