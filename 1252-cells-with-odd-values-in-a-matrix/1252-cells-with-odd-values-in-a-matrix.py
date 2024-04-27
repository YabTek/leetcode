class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        
        for a,b in indices:
            row[a] += 1
            col[b] += 1
            
        return sum((row[i] + col[j]) % 2 for i in range(m) for j in range(n))

        