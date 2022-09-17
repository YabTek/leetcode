class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = []
        queue.append(len(nums)-1)
        ans = [0] * len(nums)
        ans[len(nums)-1] = nums[len(nums)-1]
       
        for i in range(len(nums)-2,-1,-1):
            if queue[0]-i > k:
                queue.pop(0)
            ans[i] = nums[i]+ans[queue[0]]
            while queue and ans[queue[-1]]<ans[i]:
                del queue[-1]
            queue.append(i)
        return ans.pop(0)