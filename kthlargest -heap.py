import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        result  = heapq.nlargest(k,nums)
        return result[-1]
        