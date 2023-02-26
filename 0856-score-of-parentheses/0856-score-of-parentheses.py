class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        ans = 0  
        for char in s:
            if char == "(":
                stk.append(ans)
                ans = 0
            elif stk and char == ")":
                    cur = stk.pop()
                    ans = cur + max(1,2*ans)  
        return ans
        