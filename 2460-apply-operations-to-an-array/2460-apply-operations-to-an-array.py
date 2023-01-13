class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        read = 0
        write = 0
        n = len(nums)
        
        while read < n-1 and write < n-1:
            if nums[read] == nums[read+1]:
                nums[write] *= 2
                nums[write+1] = 0
            write += 1
            read += 1
            
        write = 0
        for  read in range(len(nums)):
            if nums[read] != 0:
                nums[write],nums[read] = nums[read],nums[write]
                write += 1
                
        return nums
            
        
        