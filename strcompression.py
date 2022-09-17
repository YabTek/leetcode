class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        count = Counter(chars)
        lst = ""
        ans = 0
        for key in count:
            if count[key] == 1:
                lst+=key
                ans+=1
                continue
            lst+=key
            
          
            lst+=str(count[key])
            ans+=2
        print(lst)  
        return len(lst)