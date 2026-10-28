class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        start = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "*":
                    start = [r, c]
                    break
            if start:
                break

        def bfs(r, c):

            q = collections.deque()
            q.append((r, c, 0))
            visit.add((r, c))

            while q:
                row, col, dist = q.popleft()
                if grid[row][col] == "#":
                    return dist

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and grid[r][c] != "X"):
                        visit.add((r, c))
                        q.append((r, c, 1 + dist))
            
            return -1
            
        return bfs(start[0], start[1])
