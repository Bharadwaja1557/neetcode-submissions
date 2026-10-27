class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]      # (t/max-height, r, c)
        visit.add((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == N-1 and c == N-1:
                return t
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                if row < 0 or col < 0 or row == N or col == N or (row, col) in visit:
                    continue
                
                visit.add((row, col))
                heapq.heappush(minHeap, [max(t, grid[row][col]), row, col])