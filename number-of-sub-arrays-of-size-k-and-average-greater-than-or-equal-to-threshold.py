class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        i = 0
        j = k-1
        total = sum(arr[i:j])
        for idx in range(j, len(arr)):
            total += arr[idx]
            avg = total / k
            if avg >= threshold:
                ans += 1
            total -= arr[idx - k + 1]
        return ans
       