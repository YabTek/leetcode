class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        queue = deque()
        order = []
    
            
        for i in range(len(supplies)):
            in_coming[supplies[i]] = 0
             
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                in_coming[recipes[i]] = len(ingredients[i])
        
        for recipe,incoming in in_coming.items():
            if incoming == 0:
                queue.append(recipe)
                
        while queue:
            
            recipe = queue.popleft()
            
            
            if recipe in recipes:
                order.append(recipe)
            
            for neighbour in graph[recipe]:
                    in_coming[neighbour] -= 1

                    if in_coming[neighbour] == 0:
                        queue.append(neighbour)
                    
        return order
                    
                    
                
        
        
            
        