class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        directions = ((1,0), (0,1), (-1, 0), (0, -1))
        num_islands = 0

        def dfs(row, col):

            if (row not in range(ROWS) or
            col not in range(COLS) or
            grid[row][col] == '0' or
            (row, col) in visited):
                return

            visited.add((row,col))

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row,col) not in visited:
                    num_islands += 1
                    dfs(row, col)


        return num_islands
        