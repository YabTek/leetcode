import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []

        for key, val in Counter(s).items():
            heap.append((-val, key))
        heapq.heapify(heap)

        ans = []
        last_count = 0
        last_char = ""

        while heap:
            cur_count, cur_char = heapq.heappop(heap)
            ans.append(cur_char)

            if last_count < 0:
                heapq.heappush(heap, (last_count, last_char))

            last_count = cur_count + 1
            last_char = cur_char

        return "" if last_count < 0 else "".join(ans)
        