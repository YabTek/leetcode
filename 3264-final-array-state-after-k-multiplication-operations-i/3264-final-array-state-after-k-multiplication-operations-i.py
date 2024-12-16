class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        
        while k:
            num, i = heapq.heappop(heap)
            new_num = multiplier * num
            
            nums[i] = new_num
            heapq.heappush(heap, (new_num, i))     
            k -= 1
       
            
        return nums
            
        
        