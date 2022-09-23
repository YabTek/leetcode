class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        n = len(security)-1
        prev = [0] * (n+1)
        nxt = [0] * (n+1)
        for i in range(n-1):
            if security [i] >= security [i+1]:   
                prev[i+1] = prev[i] +1 
        for j in range(n-1,-1,-1):
            if security[j] <= security [j+1]:
                nxt[j]=nxt[j+1]+1
        for k in range(n+1):
            if k < time:
                continue
            if prev[k] >= time and nxt[k] >= time:
                result.append(k)
            if k > n+1-time:
                break
        return result 