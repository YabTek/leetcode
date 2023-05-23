class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:   
        parent = {i : i for i in range(len(accounts))}
        ans = []
        emails = {}

        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            parent[xrep] = yrep
          
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email not in emails:
                    emails[email] = i
                else:
                    union(i,emails[email])
                    
        temp = defaultdict(list)
        
        for key,val in emails.items():
            temp[find(val)].append(key)
            
        for i in temp:
            name = accounts[i][0]
            emails = sorted(temp[i]) 
            ans.append([name] + emails)
            
        return ans
       