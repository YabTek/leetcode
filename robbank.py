class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        n = len(security)
        prev = [0] * n
        nxt = [0] * n
        for i in range(n):
            if security [i] <= security [i-1]:
                
                prev[i] = prev[i-1] +1 
        for j in range(n-2,-1,-1):
            if security[j+1] >= security [j]:
                nxt[j]=nxt[j+1]+1
        for k in range(time,n-time):
            if prev[k] >= time and nxt[k] >= time:
                result.append(k)
        return result