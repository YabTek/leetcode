class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]: 
       
        def dfs(node):
            visited.add(node)
            
            counter = defaultdict(int)
            counter[labels[node]] += 1

            for neighbour in graph[node]:
                if neighbour not in visited:
                    for letter,count in dfs(neighbour).items():
                        counter[letter] += count

            ans[node] = counter[labels[node]]

            return counter
        
        graph = defaultdict(list)
        ans = [1]*n
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

       
        dfs(0)
        return ans
        