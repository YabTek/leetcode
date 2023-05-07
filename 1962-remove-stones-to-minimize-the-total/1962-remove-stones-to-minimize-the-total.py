class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] = -1*piles[i]
        heapq.heapify(piles)
        
        for i in range(k):
            pile = -1*heapq.heappop(piles)
            heapq.heappush(piles,-(pile-pile//2))
            
        return -1 * sum(piles)
            
       
