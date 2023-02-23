class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        presum = 0
        cnt = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum%k == 0:
                cnt += 1
            if presum % k in d:
                cnt += d[presum%k]
            d[presum%k] += 1
        return cnt
            
        