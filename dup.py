from collections import Counter
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        n = int(len(arr)/2)
        count = 0
        sum = 0
        duplicate = Counter(arr)

        for key in duplicate:
            if duplicate[key] == n:
                return 1
            elif duplicate[key] > n:
                return 1
            else:
                sum += duplicate[key]
                count += 1
                if sum >= n:
                    
                    return count