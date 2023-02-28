class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums) + 1)
        ans = 0
        
        for start,end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1
        prefix.pop()
       
        for i in range(len(prefix)-1):
            prefix[i+1] += prefix[i]
        nums.sort()
        prefix.sort()
        
        for i in range(len(nums)):
            ans += (nums[i]*prefix[i])
            
        return (ans)%(10**9+7)
        
        