class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        directions = set([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])

        def dfs(
            pos: tuple[int, int],
            visited: set[tuple[int, int]],
            prev: int
        ) -> None:
            x, y = pos[0], pos[1]
            if (
                (x, y) in visited or
                x < 0 or y < 0 or
                x == m or y == n or
                heights[x][y] < prev
            ):
                return

            visited.add((x, y))
            for i, j in directions:
                dfs((x + i, y + j), visited, heights[x][y])

        for i in range(m):
            dfs((i, 0), pacific, heights[i][0])
            dfs((i, n-1), atlantic, heights[i][n-1])

        for j in range(n):
            dfs((0, j), pacific, heights[0][j])
            dfs((m-1, j), atlantic, heights[m-1][j])

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res

