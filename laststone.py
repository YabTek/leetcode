class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            result = 0
        elif len(stones) == 1:
            result = 1
        queue = []
        for weight in stones:
            heapq.heappush(queue,-weight)
        print(queue)
        while len(queue) > 1:  

            larger = heapq.heappop(queue)
            print(larger)
            smaller = heapq.heappop(queue)
            print(smaller)
            if larger != smaller:
                if larger>smaller:
                    heapq.heappush(queue,-(larger-smaller))
                else:
                    heapq.heappush(queue,-(smaller-larger))
            print(queue)  

        if len(queue) == 0:
               result = 0
        else:
               result = -heapq.heappop(queue)
               
        if result < 0:
            return -result
        else:
            return result