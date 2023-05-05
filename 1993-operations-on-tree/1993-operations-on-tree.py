class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.visited = [[0,0]] * len(self.parent)
        self.graph = defaultdict(list)
        
        for i in range(len(self.parent)):
            self.graph[self.parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.visited[num][0] != "locked":
            self.visited[num] = ["locked",user]
            return True
        
    def unlock(self, num: int, user: int) -> bool:
        if self.visited[num] == ["locked",user]:
            self.visited[num] = ["unlocked",user]
            return True

    def upgrade(self, num: int, user: int) -> bool:
        
        temp = num
        while temp != -1:
            if self.visited[temp][0] == "locked":
                return False
            temp = self.parent[temp]
            
        
        stack = [num]
        locked_flag = False
        
        while stack:
            node = stack.pop()
         
            for neighbour in self.graph[node]:
                if self.visited[neighbour][0] == "locked":
                    locked_flag = True
                    self.visited[neighbour][0] = "unlocked"
                stack.append(neighbour)
        
        if locked_flag:    
            self.visited[num] = ["locked",user]
            return True
            
        return False
                    
            
      

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)