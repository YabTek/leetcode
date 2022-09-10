class MedianFinder:

    def init(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 0
       
    def addNum(self, num: int) -> None:
        
            if num >= self.median:
                heapq.heappush(self.min_heap,num)
            else:
                heapq.heappush(self.max_heap,num)
               
                heapq._heapify_max(self.max_heap)
            len1 = len(self.min_heap)+1
            len2 = len(self.max_heap)+1
            
            if len2 > len1:
                    temp = heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap,temp)
                    heapq._heapify_max(self .max_heap)
            elif len1>len2:
                    temp = heapq.heappop(self.min_heap)

                    heapq.heappush(self .max_heap,temp)
                    heapq._heapify_max(self.max_heap)
                

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0])
        elif len(self.min_heap) > float(len(self.max_heap)):

            return float(self.min_heap[0])
        else:
            return float((self.min_heap[0] + self.max_heap[0])/2)
          