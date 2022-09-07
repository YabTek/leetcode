class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = Counter(words)
        result = []
        store = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        print (store)
        
        for item in store:
            result.append(item[0])
            if len(result) == k:
                return result

        #using heap

        #for i in dictionary:

         #   heap = [(-dictionary[i], i)]

      #  heapq.heapify(heap)

      #  return [heapq.heappop(heap)[1] for _ in range(k)]