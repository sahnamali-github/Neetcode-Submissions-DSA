class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxA = 0
        def bfs(r, c):
            q = deque([(r,c)])
            grid[r][c] = 0
            count = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    count += 1
            return count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxA = max(maxA, bfs(r, c))
        return maxA
        