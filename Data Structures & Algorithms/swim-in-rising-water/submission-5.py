from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = set([
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1), # right
        ])

        start = (0, 0)
        q = deque([(start, grid[0][0], {})])
        res = 2501
        while q:
            pos, t, v = q.popleft()
            x, y = pos[0], pos[1]
            if x == n-1 and y == n-1:
                if t < res:
                    res = t

                continue

            if pos in v:
                t_visited = v[pos]
                if t_visited > t:
                    v[pos] = t

                else: # t_visited <= t
                    continue
            
            else: # pos not in v
                v[pos] = t

            for i, j in directions:
                if (
                    (x+i >= 0 and x+i <= n-1) and
                    (y+j >= 0 and y+j <= n-1)
                ):
                    q.append(((x+i, y+j), max(grid[x+i][y+j], t), v))
                    # if grid[x+i][y+j] >= t:
                    #     q.append(((x+i, y+j), grid[x+i][y+j], v))

                    # else: # grid[x+i][y+j] < t
                    #     q.append(((x+i, y+j), t, v))

        return res
