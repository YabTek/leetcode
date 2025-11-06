class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i+k])
            count = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
            
            tot = 0
            for j in range(min(x, len(count))):
                tot += (count[j][0] * count[j][1])
            ans.append(tot)

        return ans




       




        