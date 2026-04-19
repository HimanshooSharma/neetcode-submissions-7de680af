class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]  # color we want to replace

        # nothing to do if color is already the target color
        if starting_color == color:
            return image

        def dfs(r, c):
            # bound check or not the original color want to replace
            if (
                not (0 <= r < len(image)) 
                or not (0 <= c < len(image[0]))
                or image[r][c] != starting_color
            ):
                return

            dirs = [(1,0),(0,1),(-1,0),(0,-1)]

            image[r][c] = color
            for dr, dc in dirs:
                dfs(r + dr,  c + dc)
        dfs(sr, sc)
        return image