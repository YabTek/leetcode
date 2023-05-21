class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        final = []
        for row in range(len(mat)):
            count = 0
            for num in mat[row]:
                if num == 1:
                    count += 1
            ans.append((count,row))
            
        ans.sort()
        
        for i in range(k):
            final.append(ans[i][1])
            
        return final
            
        
        