class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for i in range(len(s)):        
              if (s[i] == '('):
                   stk.append(i)
              elif (s[i] == ')'):
                    temp = s[stk[-1]:i + 1]
                    s = s[:stk[-1]] + temp[::-1] + s[i + 1:]
                    del stk[-1]
    # To store the modified string
        answer = ""
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                answer += (s[i])

        return answer