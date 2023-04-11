class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        
        def inbound(r, c):
            return (0 <= r < len(image) and 0 <= c < len(image[0]))
        
        def dfs(visited, r, c):
            visited[r][c] = True
            for row_change, col_change in directions:
                
                new_row = r + row_change
                new_col = c + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    if  image[new_row][new_col] == original:
                        image[new_row][new_col] = color
                        dfs(visited, new_row, new_col)

                        
        original = image[sr][sc]
        dfs(visited,sr,sc)
        
        image[sr][sc] = color
        
        return image

