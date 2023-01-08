class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        for idx,num in enumerate(nums):
            d[num] = idx
        for num,new_num in operations:
            if num in d:
                nums[d[num]] = new_num
                d[new_num] = d[num]
                
        return nums