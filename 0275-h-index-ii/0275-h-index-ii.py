class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)-1
        n = len(citations)
      
        while low <= high:
            mid = (low+high)//2
            
            if citations[mid] < n-mid:
                low = mid + 1
            else:
                high = mid - 1
                
        return len(citations) - low
