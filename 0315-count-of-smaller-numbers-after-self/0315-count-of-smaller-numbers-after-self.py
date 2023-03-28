class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(start,end,arr):
            if start == end:
                return [arr[start]]
            
            mid = (start + end)//2
            left_half = mergesort(start,mid,arr)
            right_half = mergesort(mid + 1,end,arr)
            
            for num in left_half:
                binarysearch(num,right_half)
                
            return merge(left_half,right_half)
        
        def binarysearch(num,lst):
            low = 0
            high = len(lst) - 1
            
            while low <= high:
                mid = (low + high)//2
                if lst[mid][0] >= num[0]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            ans[num[1]] += low

        def merge(arr1,arr2):
            new_arr = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    new_arr.append(arr1[i])
                    i += 1
                else:
                    new_arr.append(arr2[j])
                    j += 1
            new_arr.extend(arr1[i:])
            new_arr.extend(arr2[j:])

            return new_arr
        
        count = defaultdict(int)
        n = len(nums)
        ans = [0] * n
        
        for idx,num in enumerate(nums):
            nums[idx] = [num,idx]
      
        mergesort(0,n-1,nums)
        
        return ans