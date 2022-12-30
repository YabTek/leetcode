class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        i = 0
        ans = [0] * len(queries)
        total = sum(filter(lambda x: x%2 == 0, nums))

        for num,idx in queries:
            if nums[idx]%2 == 0:
                total -= nums[idx]   
            nums[idx] = num + nums[idx]
            if nums[idx]%2 == 0:
                total += nums[idx] 
            ans[i] = total
            i+=1
                    
        return ans
                
                
            
        
        