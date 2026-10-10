class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        q = deque()
        
        def addRoom(r,c):
            if (r < 0 or r == rows or c < 0 or c == columns
                or grid[r][c] == -1 or (r,c) in visited):
                return
            q.append((r,c))
            visited.add((r,c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q: 
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addRoom(r-1,c)
                addRoom(r,c-1)
                addRoom(r+1,c)
                addRoom(r,c+1)
            dist += 1
