class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        flip = [float('inf')] * n
        flipnot = [float('inf')] * n

        flip[0] = 1
        flipnot[0] = 0

        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                flipnot[i], flip[i] = min(flipnot[i], flipnot[i - 1]), min(flip[i], flip[i - 1] + 1)

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                flipnot[i], flip[i] = min(flipnot[i], flip[i - 1]), min(flip[i], flipnot[i - 1] + 1)

        return min(flipnot[-1], flip[-1])
