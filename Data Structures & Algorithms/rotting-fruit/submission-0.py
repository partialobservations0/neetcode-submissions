class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = [[-1 for _ in range(cols)] for _ in range(rows)]
        visited = set()

        def appendNeighbor(i,j,curr_time):
            if (i < 0 or i >= rows or j < 0 or j >= cols
            or (i,j) in visited or grid[i][j] != 1):
                return
            time[i][j] = curr_time + 1
            grid[i][j] = 2
            visited.add((i,j))
            q.append((i,j))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    time[i][j] = 0
                    visited.add((i,j))
                    q.append((i,j))

        while q: 
            i,j = q.popleft()
            appendNeighbor(i-1,j,time[i][j])
            appendNeighbor(i+1,j,time[i][j])
            appendNeighbor(i,j-1,time[i][j])
            appendNeighbor(i,j+1,time[i][j])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return max(0, max(max(x) for x in time))



