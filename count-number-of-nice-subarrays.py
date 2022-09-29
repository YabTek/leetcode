class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dictionary = defaultdict(int)
        counter = 0
        prefixsum = 0
        for i,num in enumerate(nums):
            if num%2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
        print(nums)
        for num in nums:
            prefixsum+=num
            if prefixsum == k:
                counter+=1
            if prefixsum - k in dictionary:
                counter += dictionary [prefixsum - k]
            dictionary [prefixsum] += 1
        return counter