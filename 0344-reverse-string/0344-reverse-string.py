class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1
        Solution.swap(s,start,end)
        
    def swap(s,start,end):
        if start >= end:
            return s
        else:
            s[start],s[end] = s[end],s[start]
            return Solution.swap(s,start+1,end-1)
           