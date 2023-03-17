class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    
        def find(start,end,interval,idx):
            while start < end:
                mid = (start + end) // 2
              
                if store[mid][0][0] < interval[1]:
                    start = mid+1
                else:
                    end = mid
            if start < n and store[start][0][0] >= interval[1]:
                 ans[idx] = store[start][1]
                    
            return ans
    
        n = len(intervals)
        ans = [-1] * n
        store = []
        
        for idx,interval in enumerate(intervals):
            store.append((interval,idx))
 
        store.sort()    
        i = 0    
        
        for interval,idx in store:
            start = i
            end = n
            final = find(start,end,interval,idx)
            i+=1
         
        return final
          
        