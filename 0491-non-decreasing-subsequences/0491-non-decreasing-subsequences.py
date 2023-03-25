class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start,ans):
           
            if len(ans) >= 2 and isIncreasing(ans) and ans not in final:
                final.append(ans.copy())
                
            for i in range(start,len(nums)):
                ans.append(nums[i])
                backtrack(i + 1,ans)
                ans.pop()
                
            return final
        
        def isIncreasing(ans):
            for i in range(len(ans)-1):
                if ans[i] > ans[i+1]:
                    return False
            return True

     
        final = []
        return backtrack(0,[])
        