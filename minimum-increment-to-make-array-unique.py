class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        move = 0
        nums.sort()
        size = len(nums)-1
        temp = nums[0]

        cur = 1
        while cur <= size:
            temp +=1
            if temp <= nums[cur]:
                temp = nums[cur]
            else:
                move += temp - nums[cur]
            cur += 1

        return move