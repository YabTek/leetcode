class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        ans = [0] * len(nums)
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        while k:
            num, i = heapq.heappop(heap)
            heapq.heappush(heap, (multiplier * num, i))     
            k -= 1
            
        for num, i in heap:
            ans[i] = num
            
        return ans
            
        
        