class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for j in range(len(nums2)):                                  
            heapq.heappush(heap, (nums1[0]+nums2[j], 0, j))          
        
        for _ in range(k):
            
            if heap: 
                total,i,j = heapq.heappop(heap)                       
                ans.append([nums1[i],nums2[j]])                         
            if i < len(nums1)-1:                                     
                heapq.heappush(heap, (nums1[i+1]+nums2[j],i+1, j))       

        return ans
         