class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        start = 0

        while start<k:
            nums.insert(0,nums[-1])
            del nums[-1]
            start+=1