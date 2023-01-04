class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for col in zip(*grid):
                 if tuple(row) == col:
                        count += 1
        return count
        