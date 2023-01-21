class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        ans = 0
        for i in range(1, n - 1):
            if arr[i + 1] < arr[i] > arr[i - 1]:
                l = r = i
                while l and arr[l] > arr[l - 1]: 
                    l -= 1
                while r + 1 < n and arr[r] > arr[r + 1]:
                     r += 1
                ans = max(r-l+1,ans)
               
        return ans == len(arr)
        