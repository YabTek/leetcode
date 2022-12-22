class Solution:
    def average(self, salary: List[int]) -> float:
        tot = sum(salary)
        count = len(salary) - 2
        
        minimum = min(salary)
        maximum = max(salary)
        tot -= (minimum+maximum)  
        
        return tot/count
            
        