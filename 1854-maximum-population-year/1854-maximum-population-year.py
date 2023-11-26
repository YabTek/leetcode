class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = [0] * 101
        
        for a,b in logs:
            d[a-1950] += 1
            d[b-1950] -= 1
            
        max_ = 0
        sum_ = 0
        ans = 0
        
        for i in range(len(d)):
            sum_ += d[i]
            if sum_ > max_:
                max_ = sum_
                ans = i
                
        return 1950 + ans
                
      