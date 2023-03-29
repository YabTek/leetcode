class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def quicksort(start, end):
            if start >= end:
                return
            pivot = start
            write = pivot + 1
            
            for read in range(start+1,end):
                if count[read][0] > count[pivot][0]:
                    count[read],count[write] = count[write],count[read]
                    write += 1
            count[write-1],count[pivot] = count[pivot],count[write-1]
           
            if write - 1 > k:
                quicksort(start,write-1)
            if write - 1 < k:
                quicksort(write,end)
            
               

        count = []
        ans = []
        d = Counter(nums)

        for num,cnt in d.items():
            count.append([cnt,num])
            
        quicksort(0, len(count) - 1)
        
        for lst in count[:k]:
            ans.append(lst[1])
            
        return ans
        