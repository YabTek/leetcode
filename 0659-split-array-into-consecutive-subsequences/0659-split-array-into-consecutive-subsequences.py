class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = defaultdict(list)

        for i in nums:
            prev = i-1
            if len(d[prev]) >= 1:
                temp = heapq.heappop(d[prev])
                heapq.heappush(d[i], temp+1)
            else:
                heapq.heappush(d[i], 1)
            
               
        flag = True

        for i in d.values():
            if i and i[0] < 3:
                flag = False

        return flag
        