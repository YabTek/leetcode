class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        mod = 10**9+7
        hash_map = defaultdict(int)
        
        for i in range(len(deliciousness)): 
            for j in range(22):
                pwr = math.pow(2,j)
                ans += hash_map[pwr - deliciousness[i]]
                
            hash_map[deliciousness[i]] += 1
            
        return ans % mod
            
       
        
        

          
       