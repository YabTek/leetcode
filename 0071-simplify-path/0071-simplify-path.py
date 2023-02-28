class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
      
        for char in path.split("/"):
            if stk and char == "..":
                stk.pop()
            elif char == "" or char == "." or char == "..":
                continue
            else:
                stk.append(char)

        return "/" + "/".join(stk)
                
        