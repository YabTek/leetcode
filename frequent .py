from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary = Counter(nums)
        result = []
        store = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        for item in store:
            result.append(item[0])
            if len(result) == k:
                return result