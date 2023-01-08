class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = ['#'] * len(nums)
        left = 0
        right = len(nums)-1
        
        for num in nums:
            if num < pivot:
                ans[left] = num
                left += 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > pivot:
                ans[right] = nums[i]
                right -= 1
        for i,num in enumerate(ans):
            if num == '#':
                ans[i] = pivot
        return ans
                
        