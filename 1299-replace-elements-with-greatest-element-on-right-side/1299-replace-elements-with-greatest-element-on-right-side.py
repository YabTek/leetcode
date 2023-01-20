class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-2
        last = arr[-1]
        arr[-1] = -1
     
        while i >= 0:
            arr[i],last = last, max(last,arr[i])
            i -= 1
            
        return arr

        