class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ans = True
        n = len(equations)
        parent = {chr(i+97) :  chr(i+97) for i in range(26)}
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep:
                return
            parent[yrep] = xrep
            
        def isConnected(x,y):
            return find(x) == find(y)
        
        for i in range(n):
            if equations[i][1] == "=":
                union(equations[i][0],equations[i][3])
                
        for i in range(n):
            char1 = equations[i][0]
            char2 = equations[i][1]
            char3 = equations[i][3]
            
            if equations[i][1] == "!" and isConnected(char1,char3):
                ans = False
                
        return ans      
            
            