class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        store = []
       
        idx = 0
        while idx < n:
            if nums[idx]%2 != 0:
                store.append(idx)          
            idx += 1
        store.append(n)
 
        size = len(store)
        if k < size:
            temp = store[k] - store[k-1]
            ans +=  (store[0] + 1) * temp
        j = k+1
        while j < size:
            diff = j-k
            ans += (store[diff] - store[diff-1]) * (store[j] - store[j-1])
            j+=1
 

        return ans