class Solution:

    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        size = len(nums)
        temp = []
        pair1 = 0
        pair2 = size-1
        while pair1 < pair2:
            temp.append(nums[pair1]+nums[pair2])
            pair1 += 1
            pair2 -= 1
        return max(temp)