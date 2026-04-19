class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        directions = ((1,0), (0,1), (-1,0), (0,-1))

        visited = set()

        max_area = 0

        def dfs(row, col):
            if (row not in range(ROWS) or
            col not in range(COLS) or
            grid[row][col] == 0 or
            (row,col) in visited):
                return 0
            
            visited.add((row, col))
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area, dfs(row,col))
        
        return max_area
