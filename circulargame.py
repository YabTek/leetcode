class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque()
        for i in range(1,n+1):
            queue.append(i)
            
        while len(queue) > 1:       
            for i in range(k-1):   
                temp = queue.popleft()
                queue.append(temp)
            queue.popleft()
        return queue[0]
