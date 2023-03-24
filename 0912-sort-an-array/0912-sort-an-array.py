class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(left, right,nums):
            if left == right:
                return [nums[left]]
            mid = (left+right)//2
            left_half = mergesort(left,mid,nums)
            right_half = mergesort(mid+1,right,nums)
            
            return merge(left_half,right_half)
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
        
        return mergesort(0,len(nums)-1,nums)
                    
          
           
        
