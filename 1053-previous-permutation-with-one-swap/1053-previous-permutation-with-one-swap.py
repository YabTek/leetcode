class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pause = None
        
        for i in range(n-1,0,-1):
            if arr[i-1] > arr[i]:
                pause = i-1
                break
                
        if pause == None: 
            return arr

        for i in range(n-1,pause,-1):
            if arr[i] < arr[pause] and arr[i] != arr[i-1]:
                arr[i],arr[pause] = arr[pause],arr[i]
                break

        return arr
