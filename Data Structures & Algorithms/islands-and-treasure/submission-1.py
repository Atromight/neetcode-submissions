from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        treasures = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasures.add((i, j))
        
        directions = set([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])

        for treasure in treasures:
            x = treasure[0]
            y = treasure[1]
            steps = 0
            visited = set()
            q = deque([(x, y, steps)])
            while q:
                x, y, s = q.popleft()
                visited.add((x, y))
                if grid[x][y] > s:
                    grid[x][y] = s

                for i, j in directions:
                    if (
                        (x + i) >= 0 and (x + i) < m and
                        (y + j) >= 0 and (y + j) < n and
                        grid[x+i][y+j] != -1 and
                        grid[x+i][y+j] != 0 and
                        (x+i, y+j) not in visited
                    ):
                        q.append((x+i, y+j, s+1))

