
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(31, -1, -1):
            temp = ans | (1 << i)
            store = set(temp & j for j in nums)
            
            if any(j ^ temp in store for j in store): 
                ans = temp
                
        return ans