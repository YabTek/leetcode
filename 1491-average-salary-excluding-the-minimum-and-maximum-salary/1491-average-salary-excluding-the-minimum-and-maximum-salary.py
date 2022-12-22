class Solution:
    def average(self, salary: List[int]) -> float:
        tot = 0
        cnt = len(salary) - 2
        minimum = min(salary)
        maximum = max(salary)
        
        for value in salary:
            tot += value
        tot -= (minimum+maximum)  
        return tot/cnt
            
        