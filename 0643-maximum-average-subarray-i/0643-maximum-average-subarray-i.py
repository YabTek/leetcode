class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = sum(nums[:k])
        first_avg = tot/k
        max_avg= first_avg
        j = 0
        for i in range(k,len(nums)):
            tot += nums[i]-nums[j]
            avg = tot/k
            max_avg = max(max_avg,avg)
            j+=1
        return max_avg
