import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = Counter(nums)
 
        heap = []
        ans = []
       # result = []

       # store = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
      #  for item in store:
           # result.append(item[0])
           # if len(result) == k:
             #   return result
        #using heap
        for key,val in dictionary.items():
            heapq.heappush(heap, ([val,key]))
 
        temp = heapq.nlargest(k,heap)    

        for i in temp:
            ans.append(i[1])
        return ans
         #approach3 
       # for key,val in dictionary.items():

        #    heapq.heappush(heap, ([-val,key]))


      #  heapq.heapify(heap)   
      #  lst = []
        #for i in range(k):
       #     temp = heapq.heappop(heap)
        #    lst.append(temp)
      
       # for j in lst:
         #   ans.append(j[1])
        
       # return ans