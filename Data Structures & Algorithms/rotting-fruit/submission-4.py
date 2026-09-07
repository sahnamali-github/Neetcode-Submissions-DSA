class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # q = deque()
        # fresh = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 2:
        #             q.append((r,c))
        #         if grid[r][c] == 1:
        #             fresh += 1
        # if fresh == 0:
        #     return 0
        # minutes = 0
        
        # def addRoom(r, c):
        #     nonlocal fresh
        #     if min(r,c)<0 or r >= rows or c >= cols or grid[r][c] != 1:
        #         return
        #     grid[r][c] = 2
        #     q.append((r,c))
        #     fresh -= 1

        # while q and fresh:
            
        #     for i in range(len(q)):
        #         r, c = q.popleft()
        #         addRoom(r, c + 1)
        #         addRoom(r, c - 1)
        #         addRoom(r + 1, c)
        #         addRoom(r - 1, c)
        #     minutes += 1
        # return minutes if not fresh else -1

        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= rows or nc>= cols or grid[nr][nc] != 1):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        return time if not fresh else -1

            
        