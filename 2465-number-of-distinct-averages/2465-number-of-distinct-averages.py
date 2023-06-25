class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        store = set()
        nums.sort()
        
        i = 0
        j = len(nums)-1
        
        while i < j:
            avg = (nums[i]+nums[j]) / 2
            store.add(avg)
            i += 1
            j -= 1
            
        return len(store)
            

        