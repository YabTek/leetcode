import collections 
class Solution:

    def longestSubarray(self, nums: list[int], limit: int) -> int:
        answer = 0
        temp = 0
        min_q  = collections.deque()
        max_q = collections.deque()
        for a, b in enumerate(nums):
            while len(max_q) > 0 and b > max_q[-1]:
                max_q.pop()
            while len(min_q) > 0 and b < min_q[-1]:
                min_q.pop()
            max_q.append(b)
            min_q.append(b)
            while len(max_q) > 0 and len(min_q) > 0 and max_q[0] - min_q[0] > limit:
                if nums[temp] == max_q[0]: 
                    max_q.popleft()
                if nums[temp] == min_q[0]:
                    min_q.popleft()
                temp += 1
            answer = max(answer, a - temp+ 1)
        return answer