class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapify(heap)
        
        while k > 0:
            num = -1*heappop(heap)
            heappush(heap,-1*(num-(num//2))) 
            k -= 1
            
        return -1*sum(heap)
        