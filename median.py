class MedianFinder:

    def init(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 0
       
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        if len(self.min_heap)>len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                 
    def findMedian(self) -> float:
        if len(self.max_heap) >len(self.min_heap):
            self.median = -float(self.max_heap[0]) 
        else:
            self.median = float((self.min_heap[0] +( -self.max_heap[0]))/2)
          
        return self.median
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()