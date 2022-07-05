class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    good_pairs.append((i,j))
        return len(good_pairs)
    
result = Solution()
result.numIdenticalPairs([1,2,3,1,1,3])