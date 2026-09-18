class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacSet, atlSet = set(), set()
        pac_q, atl_q = deque(), deque()
        for r in range(rows):
            pac_q.append((r, 0))
            pacSet.add((r, 0))
            atl_q.append((r, cols - 1))
            atlSet.add((r, cols - 1))
            
        for c in range(cols):
            pac_q.append((0, c))
            pacSet.add((0, c))
            atl_q.append((rows - 1, c))
            atlSet.add((rows - 1, c))
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        def bfs(queue, visitSet):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or heights[nr][nc] < heights[r][c] or (nr, nc) in visitSet:
                        continue
                    visitSet.add((nr, nc))
                    queue.append((nr, nc))
        bfs(pac_q, pacSet)
        bfs(atl_q, atlSet)
        return list(pacSet & atlSet)
        