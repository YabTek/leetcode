class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        ans = []
        row = len(mat)
        col = len(mat[0])
       
        for i in range(row):
            for j in range(col):
                d[i+j].append(mat[i][j])
                    
        for num,lst in d.items():
            if num % 2 == 0:
                lst.reverse()
                
        for lst in d.values():
            for num in lst:
                ans.append(num)
                
        return ans       