class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        token=[]
        stack = []
        i = 0
        for item in tokens:
            try:
                token.append(int(item))
            except:
                token.append(str(item))
        while i < len(token):
            if token[i] == "+":
                first = stack.pop()

                second = stack.pop()
                i+= 1
                stack.append(first+second)
            elif token[i] == '-':
                first = stack.pop()
                second = stack.pop()
                i +=1
                stack.append(second-first)
            elif token[i] == '*':
                first = stack.pop()
                second = stack.pop()
                i+=1
                stack.append(second*first)
            elif token[i] == '/':
                first = stack.pop()
                second = stack.pop()
                i+=1
                stack.append(int(second/first))
            else:
                stack.append(token[i])
                i+=1
        answer = stack[0]
        
        
        return answer