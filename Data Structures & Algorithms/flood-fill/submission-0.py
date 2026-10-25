class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        def dfs(r,c, color, prev_color):
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c) in visited or image[r][c] != prev_color):
                return 
            
            visited.add((r,c))

            dfs(r-1, c, color, image[sr][sc])
            dfs(r, c-1, color, image[sr][sc])
            dfs(r+1, c, color, image[sr][sc])
            dfs(r, c+1, color, image[sr][sc])

        dfs(sr,sc,color,image[sr][sc])
        for rc in visited:
            r,c = rc
            image[r][c] = color
        return image
