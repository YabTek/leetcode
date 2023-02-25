class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for log in logs:
            if log != "../" and log != "./":
                stk.append(log)
            if stk and log == "../":
                stk.pop()
        return len(stk)
          
                
                
                
        