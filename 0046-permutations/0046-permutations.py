class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr,ans):
            if len(ans) == len(nums):
                final.append(ans.copy())
                return
               
            for i in range(len(arr)):
                ans.append(arr[i])
                new_arr = arr[:i] + arr[i+1:]
                backtrack(new_arr,ans)
                ans.pop()
                
        final = []
        backtrack(nums,[])
        return final
    
    
        