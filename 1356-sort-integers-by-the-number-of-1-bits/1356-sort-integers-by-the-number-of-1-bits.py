class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def countOnes(num):
            return (bin(num)[2:]).count("1")
        
        return sorted(arr, key=lambda num: (countOnes(num), num))

       

        
        