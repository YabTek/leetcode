class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]: 
       
        def dfs(node):
           
            counter = defaultdict(int)
            counter[labels[node]] += 1

            for neighbour in graph[node]:
                graph[neighbour].remove(node)

                for key, val in dfs(neighbour).items():
                    counter[key] += val

            ans[node] = counter[labels[node]]
            
            return counter
        
        graph = defaultdict(list)
        ans = [1]*n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

       
        dfs(0)
        return ans
        