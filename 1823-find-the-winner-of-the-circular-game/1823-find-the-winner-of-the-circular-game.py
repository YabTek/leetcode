class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        idx = 0
        
        while True:
            if len(arr) == 1:
                break
            idx = (idx+k-1) % len(arr)
            arr.pop(idx)
            
        return arr[0]
            
        