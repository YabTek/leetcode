class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        idx = 0
        n = len(nums)
        while i < n:
            while j<n and  nums[i] == nums[j]:
                j+=1
            nums[idx] = nums[i]
            idx += 1
            i = j
        return idx