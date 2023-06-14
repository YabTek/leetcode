class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) 
        visited = set([(0,1,0)])
            
        while queue:
            position, speed, steps = queue.popleft()
            
            if position == target:
                return steps
            
            if (position,speed) not in visited:
                visited.add((position, speed))
                queue.append((position+speed, speed*2, steps+1))
                
                if speed > 0:
                    queue.append((position, -1, steps+1))
                else:
                    queue.append((position, 1, steps+1))

