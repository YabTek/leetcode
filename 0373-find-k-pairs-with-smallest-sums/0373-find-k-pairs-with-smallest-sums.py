class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []
        n = len(nums1)
        m = len(nums2)
        
        for i in range(n):
            heappush(heap,(nums1[i] + nums2[0],i,0))
            
        for _ in range(k):
            if heap:
                tot,i,j = heappop(heap)
                ans.append([nums1[i],nums2[j]])
            
            if j < m-1:
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                
        return ans
            
            
       