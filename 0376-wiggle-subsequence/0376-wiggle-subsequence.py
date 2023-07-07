class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        d = {}

        def dp(i, up):
            if (i,up) in d:
                return d[(i,up)]

            max_length = 1
            for j in range(i + 1, n):
                if (up and nums[j] < nums[i]) or (not up and nums[j] > nums[i]):
                    max_length = max(max_length, 1 + dp(j, not up))

            d[(i,up)] = max_length
            return max_length

        return max(dp(0, True), dp(0, False))
