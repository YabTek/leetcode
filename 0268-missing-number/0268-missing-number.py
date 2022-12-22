class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
       
        for num in range(len(nums)+1): 
            if num in nums:
                hash_table[num] += 1
            else: 
                 hash_table[num] = 0
                
        for num,count in hash_table.items():
            if count == 0:
                return num
            
                    
        