class Solution:
    def isValid(self, s:str) -> bool:
        bracket_open = '('
        bracket_close = ')'
        curly_open = '{'
        curly_close = '}'
        square_open = '['
        square_close = ']'
        
        stack = []
        store = { 
             "[":"]","(" : ")", "{" : "}"
                 }
        for symbols in s:
            if symbols == bracket_open or symbols == curly_open or symbols == square_open:
                stack.append(symbols)
            elif len(stack) > 0:
                opening = stack.pop()
                if store[opening] != symbols:
                    return False
            else:
                return False
        return len(stack) == 0
     
            
result = Solution()
result.isValid("{[]}")
        