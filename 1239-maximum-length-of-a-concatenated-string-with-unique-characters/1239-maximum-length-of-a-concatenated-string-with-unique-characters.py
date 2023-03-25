class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def backtrack(start,ans):
            nonlocal max_
            
            string = "".join(ans)
            if isUnique(string):
                max_ = max(max_,len(string))
                
            for i in range(start,len(arr)):
                ans .append(arr[i])
                backtrack(i+1,ans)
                ans.pop()
                
            return max_
                
        def isUnique(string):
            count = Counter(string)
            if len(string) == len(count):
                return True
            return False
            
        max_ = 0
        return backtrack(0,[])
        