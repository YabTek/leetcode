class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(left,right,arr):
            if left == right:
                return [arr[left]]
            
            mid = (right + left) // 2
            left_half = mergesort(left, mid, arr)
            right_half = mergesort(mid + 1, right, arr)
           
            for num in left_half:
                binarysearch(num//2,right_half)
            return merge(left_half,right_half)
            
        def binarysearch(num,lst):
            nonlocal ans
            
            low = 0
            high = len(lst)-1
            
            while low <= high:
                mid = (low+high)//2
                if lst[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            ans += low
            
                    
            
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
            
        ans = 0
        for i in range(len(nums)):
            nums[i] *= 2
            
        mergesort(0,len(nums)-1,nums)
        return ans
    


