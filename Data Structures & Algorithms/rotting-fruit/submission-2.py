class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        
        def addRoom(r, c):
            nonlocal fresh
            if min(r,c)<0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r,c))
            fresh -= 1

        while q and fresh:
            
            for i in range(len(q)):
                r, c = q.popleft()
                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)
            minutes += 1
        return minutes if not fresh else -1
            
        