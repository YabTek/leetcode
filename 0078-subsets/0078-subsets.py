class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,ans):
            if start == n:
                final.append(ans.copy())
                return final
            ans.append(nums[start])
            backtrack(start+1,ans)
            ans.pop()
            backtrack(start+1,ans)
                            
                
        final = []
        n = len(nums)
        backtrack(0,[])
        return final
    
        