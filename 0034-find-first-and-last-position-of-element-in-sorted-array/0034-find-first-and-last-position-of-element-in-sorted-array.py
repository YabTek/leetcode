class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        flag = True
        ans = [-1,-1]
        
        while low <= high:
                mid = (low+high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid
                    high = mid
                    while low  and nums[low-1] == target:
                         low -= 1
                    while high < len(nums)-1 and nums[high+1] == target:
                         high += 1
                            
                    ans[0] = low
                    ans[1] = high
                    return ans
        return ans
        
        
        
   