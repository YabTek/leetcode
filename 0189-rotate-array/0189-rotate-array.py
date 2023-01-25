class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        left = 0
        right = len(nums)-1
        
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1 
            
        k %= len(nums)
        left = 0
        right = k-1
        
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1 
            
        left = k
        right = len(nums)-1
        
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1 
            

            

		

			
        