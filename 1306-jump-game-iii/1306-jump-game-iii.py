class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        d = {}

        @cache
        def dp(idx):

            if idx < 0 or idx >= n or idx in d:
                return False
            
            if arr[idx] == 0:
                return True

            d[idx] = "visited"

            return dp(idx + arr[idx]) or dp(idx - arr[idx])

        return dp(start)
