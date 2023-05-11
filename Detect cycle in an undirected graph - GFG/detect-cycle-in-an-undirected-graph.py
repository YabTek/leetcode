from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		colors = ["white"] * V
		
		def dfs(node,parent):
		    if colors[node] == "gray":
		        return True
		       
		    colors[node] = "gray"
		    for neighbour in adj[node]:
		        if neighbour == parent:
		            continue
		        if dfs(neighbour,node):
		            return True
		            
		    colors[node] = "black"
		    
		    return False
		    
		
		for node in range(V):
		    if colors[node] == "white":
		        if dfs(node,None):
		            return 1
		            
		return 0
		        
		        
		        



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends