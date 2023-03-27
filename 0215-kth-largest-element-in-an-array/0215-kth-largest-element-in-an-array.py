class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(start,end):
            if start >= end:
                return
            pivot = start
            write = start + 1
            
            for read in range(start+1,end):
                if nums[read] <= nums[pivot]:
                    nums[read],nums[write] = nums[write],nums[read]
                    write += 1
            nums[pivot],nums[write-1] = nums[write-1],nums[pivot]
            
            n = len(nums)
            if write - 1 > n-k:
                quicksort(start,write-1)
            elif  write - 1 < n-k:
                quicksort(write,end)
            
            return nums[n-k]
        
        return quicksort(0,len(nums))
            
            
        