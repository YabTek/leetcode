class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_zeros = []
        row_ones = []
        col_zeros = []
        col_ones = []
        ans = [[] for _ in range(len(grid))]
        
        for lst in grid:
            row_zeros.append(lst.count(0))
            row_ones.append(lst.count(1))
            
        for num in zip(*grid):
            col_zeros.append(num.count(0))
            col_ones.append(num.count(1))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[i].append(row_ones[i]+col_ones[j]-row_zeros[i]-col_zeros[j])
        return ans
            
            
        