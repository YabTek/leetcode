class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        
        for a,b in logs:
            for i in range(a,b):
                d[i] += 1
       
        sorted_ = sorted(d.items(), key=lambda x: (-x[1], x[0]))
      
        return sorted_[0][0]
        