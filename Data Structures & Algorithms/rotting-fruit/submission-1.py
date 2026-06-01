class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.add((i, j))

                grid[i][j] = - grid[i][j]

        directions = set([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])
        for x, y in rotten:
            minutes = 0
            visited = set()
            q = deque([(x, y, minutes)])
            while q:
                x, y, mins = q.popleft()
                visited.add((x, y))
                if (
                    (grid[x][y] == -1) or
                    (grid[x][y] > 0 and grid[x][y] > mins)
                ):
                    grid[x][y] = mins

                for i, j in directions:
                    if (
                        (x + i) >= 0 and (x + i) < m and
                        (y + j) >= 0 and (y + j) < n and
                        grid[x+i][y+j] != -2 and
                        grid[x+i][y+j] != 0 and
                        (x+i, y+j) not in visited
                    ):
                        q.append((x+i, y+j, mins+1))

        max_mins = 0    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    return -1
                else:
                    if grid[i][j] > 0:
                        if grid[i][j] > max_mins:
                            max_mins = grid[i][j]

        return max_mins

