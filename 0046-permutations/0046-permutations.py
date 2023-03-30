class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,ans):
            if len(ans) == len(nums):
                final.append(ans.copy())
                return
               
            for i in range(len(nums)):
                if (1 << i) & start == 0:
                    ans.append(nums[i])
                    backtrack(start | 1 << i,ans)
                    ans.pop()
                
        final = []
        backtrack(0,[])
        return final
    
    
        