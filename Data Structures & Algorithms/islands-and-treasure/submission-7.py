class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def addRoom(r, c):
            if (min(r, c) < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == -1):
                return
            q.append((r,c))
            visit.add((r,c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
            dist += 1
        

        