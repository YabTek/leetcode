class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        subarray = [nums[a:b] for a, b in combinations(range(len(nums) + 1), r=2)]
        ans = [len(subarray)+3 for _ in range(len(subarray))]
      
        for i in range(len(subarray)):
            sum = 0
            for num in subarray[i]:
                sum+=num
                if sum >= k:
                    ans[i] = len(subarray[i])
        
        if min(ans) == len(subarray)+3:
            return -1
        return min(ans)