class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        def mergesort(start,end,arr):
            if start == end:
                return [arr[start]]
            
            mid = (start + end)//2
            left_half = mergesort(start,mid,arr)
            right_half = mergesort(mid + 1,end,arr)
                
            return merge(left_half,right_half)
        
        def binarysearch(num,arr):
            low = 0
            high = len(arr) - 1
            
            while low <= high:
                mid = low + (high-low)//2
                if num + diff >= arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            if low == 0 and high < 0:
                return -1
            return low
         
        def merge(arr1,arr2):
            nonlocal ans
            
            new_arr = []
            i = 0
            j = 0
            
            for num in arr2:
                temp = binarysearch(num,arr1)
                if temp != -1:
                    ans += temp
                    
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
            

       