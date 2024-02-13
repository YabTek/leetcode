class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        
        for i in range(1,n):
            arr[i] += arr[i-1]
        arr = [0] + arr
        
        for i in range(3, n + 1, 2):
            start = 0 
            for j in range(i,n+1):
                ans += arr[j] - arr[start]
                start += 1
              
        return ans + arr[-1]