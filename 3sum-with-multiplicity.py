class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        modulo = 10**9+7
        ans = 0
        count = Counter(arr)
        
        for i in range(101):
            for j in range(i,101):
                k = target-i-j
                if k<0 or k >100:
                     continue
                if i ==j==k:
                    ans += count[i] * (count[i]-1) * (count[i]-2) /6
                
                elif i ==j != k:
                    ans += ((count[i] * (count[i]-1) /2 ) * count[k])
                
                elif i < j < k:
                    ans += (count[i] * count[j] * count[k])
            
        return int(ans%modulo)