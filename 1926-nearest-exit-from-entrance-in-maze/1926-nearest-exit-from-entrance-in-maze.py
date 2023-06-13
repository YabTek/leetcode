class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance, 0)])
        visited = set([tuple(entrance)])  
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        n = len(maze)
        m = len(maze[0])

        def isInBound(i, j):
            if 0 <= i < n and 0 <= j < m:
                return True

        while queue:
            cur = queue.popleft()
            row, col = cur[0]
            steps = cur[1]

            if [row,col] != entrance and (row in [0, n-1] or col in [0, m-1]):
                return steps

            for r, c in directions:
                nr = row + r
                nc = col + c

                if isInBound(nr, nc) and maze[nr][nc] == "." and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(([nr, nc], steps+1))

        return -1

           
        