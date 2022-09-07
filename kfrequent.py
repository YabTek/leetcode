import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = Counter(nums)
        result = []
        store = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        for item in store:
            result.append(item[0])
            if len(result) == k:
                return result
        #using heap
        #for i in dictionary:
         #   heap = [(-dictionary[i], i)]
      #  heapq.heapify(heap)
      #  return [heapq.heappop(heap)[1] for _ in range(k)]