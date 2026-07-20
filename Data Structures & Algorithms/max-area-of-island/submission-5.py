class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxA = 0
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = 0
            count = 0
            while q:
                r, c = q.popleft()
                count += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            return count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxA = max(maxA, area)
        return maxA
        