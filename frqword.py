class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = Counter(words)
        ans = []
        heap = []
        for key,val in dictionary.items():
            heapq.heappush(heap,[-val,key])
            
        heapq.heapify(heap)
        while k > len(ans):
            temp = heapq.heappop(heap)
            ans.append(temp[1])
           
        return ans