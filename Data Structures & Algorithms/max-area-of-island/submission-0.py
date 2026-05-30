class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = set([
            (0, 1), # right
            (0, -1), # left
            (1, 0), # up
            (-1, 0) # down
        ])
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        visited = set()

        def dfs(
            pos: tuple[int, int],
            visited: set[tuple[int, int]]
        ) -> int:
            i = pos[0]
            j = pos[1]
            # print(f"pos: {pos}, grid[i][j]: {grid[i][j]}")
            # print(f"area: {self.area}, visited: {visited}")
            if (i,j) not in visited:
                visited.add((i, j))
                if grid[i][j] == 1:
                    self.area += 1
                    for x, y in directions:
                        if (i + x) >= 0 and (i + x) < m and (j + y) >= 0 and (j + y) < n:
                            next_pos = (i + x, j + y)
                            # print(f"Recursing pos: {pos}, next_pos: {next_pos}")
                            dfs(next_pos, visited)
                            # print(f"Returning to recursion pos: {pos}, prev_pos: {next_pos}")
                            # print("")

                    # print(f"Returning area: {self.area}")
                    return

                else: # grid[i][j] == 0
                    return

            else:
                return


        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    # print(f"max_area: {max_area}")
                    self.area = 0
                    dfs((i,j), visited)
                    if self.area > max_area:
                        max_area = self.area

        return max_area
