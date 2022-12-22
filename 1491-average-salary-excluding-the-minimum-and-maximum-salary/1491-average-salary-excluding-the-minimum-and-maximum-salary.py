class Solution:
    def average(self, salary: List[int]) -> float:
        tot = sum(salary)
        count = len(salary) - 2
       
        tot -= (min(salary) + max(salary))  
        
        return tot/count
            
        