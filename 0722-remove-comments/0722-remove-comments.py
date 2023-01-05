class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = ""
        blockComment=False
        lineComment=False
        source="\n".join(source) 
        n = len(source)
        new=""
        i=0
        
        while i<n:
            if not blockComment and  (i+1)<n and source[i]=='/' and source[i+1]=='/':
                lineComment=True
                i+=2
                continue 
            if lineComment and  source[i]=='\n':
                lineComment=False      
            if lineComment:
                i+=1
                continue
            if not blockComment and (i+1)<n and source[i]=='/'and source[i+1]=='*':
                blockComment=True
                i+=2
                continue
            if blockComment and (i+1)<n and source[i]=='*'and source[i+1]=='/':
                blockComment=False
                i+=2
                continue
            if blockComment:
                i+=1
                continue           
            new+=source[i]            
            i+=1
            
        
        for i in range(len(new)):
            if i==0 and new[i]=='\n':
                continue
            if i>0 and new[i]=='\n' and new[i-1]=='\n':
                continue
            ans=ans+new[i]
 
        return ans.split('\n')
        