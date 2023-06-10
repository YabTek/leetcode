class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        def compare(a, b):
            if freq[a] != freq[b]:
                return freq[a] - freq[b]
            else:
                return b - a

        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        