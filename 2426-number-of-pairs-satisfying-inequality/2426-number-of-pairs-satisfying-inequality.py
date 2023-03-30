class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        def mergesort(start,end,arr):
            if start == end:
                return [arr[start]]
            
            mid = (start + end)//2
            left_half = mergesort(start,mid,arr)
            right_half = mergesort(mid + 1,end,arr)
            
            for num in right_half:
                binarysearch(num,left_half)
                
            return merge(left_half,right_half)
        
        def binarysearch(num,arr):
            nonlocal ans
            
            low = 0
            high = len(arr) - 1
            
            while low <= high:
                mid = (low+high)//2
                
                if num + diff >= arr[mid] :
                    low = mid + 1
                else:
                    high = mid - 1

            ans += low
         
        def merge(arr1,arr2):
            nonlocal ans
            
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
               
        ans = 0
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]   
        mergesort(0,len(nums)-1,nums)
        
        return ans
            

       