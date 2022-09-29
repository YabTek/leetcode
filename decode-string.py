class Solution:
    def decodeString(self, s: str) -> str:

        if len(s) == 0:
            return ""
        size = len(s)
        stk=[]    
        idx = 0
        while idx<size:
            if s[idx] != "]":
                stk.append(s[idx])
            elif s[idx] == "]":
                notnumber=[] 
                while stk and stk[-1]!="[":
                    notnumber.append(stk.pop())
                stk.pop()
                number=""
                while stk and stk[-1].isnumeric():
                    number+=stk.pop()    
                number=int(number[::-1])
                temp = "".join(notnumber[::-1])           
                stk.append(number*temp)
            idx+=1
        result = "".join(stk)

        
        return result