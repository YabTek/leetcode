class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #heap = []
       # for lst in matrix:
        #    for num in lst:
        #        heap.append(num)
        
       # heapq.heapify(heap)
       # ans = heapq.nsmallest(k,heap)
        #return ans[k-1]
        heap = matrix[0]
        for lst in matrix[1:len(matrix)]:
            heap += lst
        heapq.heapify(heap)
        ans = heapq.nsmallest(k,heap)

        return ans[k-1]